from flask import Flask, render_template, redirect, url_for, request, session, flash
import requests
from extensions import db
from models import User, Transfer, Favourite, League

app = Flask(__name__)
app.secret_key = "supersecretkey"

API_KEY = '106a2e598cb1c46f7b2149a59a1beca1'
API_HOST = 'https://v3.football.api-sports.io'
URL = f'{API_HOST}/fixtures?live=all'

HEADERS = {
    'x-apisports-key': API_KEY
}

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///transfers.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route('/matches')
def live_scores():
    response = requests.get(URL, headers=HEADERS)
    data = response.json()
    live_matches = data.get('response', [])
    return render_template('scores.html', matches=live_matches)

@app.route("/standings/<int:league_id>")
def standings(league_id):
    season = 2022
    try:
        response = requests.get(f"{API_HOST}/leagues?id={league_id}", headers=HEADERS)
        league_data = response.json()
        league_name = league_data['response'][0]['league']['name']
    except (IndexError, KeyError):
        league_name = "Unknown League"

    url = f'{API_HOST}/standings?league={league_id}&season={season}'
    res = requests.get(url, headers=HEADERS)
    data = res.json()

    try:
        if league_id > 4:
            standings = data['response'][0]['league']['standings'][0]
        else:
            standings = data['response'][0]['league']['standings']
    except (IndexError, KeyError):
        standings = []

    return render_template('standings.html', standings=standings, league_name=league_name, league_id=league_id)

@app.route("/transfers")
def transfers():
    transfers = Transfer.query.all()
    return render_template("transfers.html", transfers=transfers)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session["user"] = user.username

            if user.username == "admin":
                session["is_admin"] = True
            else:
                session["is_admin"] = False

            flash("Login successful!", "success")
            return redirect(url_for("home"))
        else:
            flash("Invalid username or password", "danger")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("You’ve been logged out.", "info")
    return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if User.query.filter_by(username=username).first():
            flash("Username already taken!", "danger")
            return redirect(url_for("register"))

        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful! You can now log in.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/admin")
def admin():
    if "user" not in session or session["user"] != "admin":
        flash("You must be admin to view this page", "warning")
        return redirect(url_for("login"))

    users = User.query.all()
    return render_template("admin.html",users=users, user=session["user"])

@app.route("/admin/delete_user/<int:user_id>", methods=["POST"])
def delete_user(user_id):
    if "user" not in session or session["user"] != "admin":
        return redirect(url_for("login"))

    user = User.query.get_or_404(user_id)
    if user.username == "admin":
        flash("You cannot delete the admin account.", "danger")
        return redirect(url_for("admin"))

    db.session.delete(user)
    db.session.commit()
    flash("User deleted successfully.", "success")
    return redirect(url_for("admin"))


@app.route("/admin/edit_user/<int:user_id>", methods=["POST"])
def edit_user(user_id):
    if "user" not in session or session["user"] != "admin":
        return redirect(url_for("login"))

    new_username = request.form.get("new_username")
    user = User.query.get_or_404(user_id)

    if new_username:
        user.username = new_username
        db.session.commit()
        flash("Username updated successfully.", "success")

    return redirect(url_for("admin"))

@app.route("/account")
def account():
    if "user" not in session:
        flash("Please log in to view your account", "warning")
        return redirect(url_for("login"))

    user = User.query.filter_by(username=session["user"]).first()
    if not user:
        flash("User not found", "danger")
        return redirect(url_for("login"))

    favs_with_logo = []
    for fav in user.favourites:
        logo = None
        if fav.fav_type == "league" and fav.league:
            logo = fav.league.logo
        favs_with_logo.append({"fav": fav, "logo": logo})

    return render_template("account.html", user=user, favourites=favs_with_logo)


@app.route("/admin/add_transfer", methods=["POST"])
def add_transfer():
    if "user" not in session or session["user"] != "admin":
        return redirect(url_for("login"))

    player = request.form.get("player")
    from_team = request.form.get("from_team")
    to_team = request.form.get("to_team")
    date = request.form.get("date")
    fee = request.form.get("fee")
    image = request.form.get("image")
    from_team_logo = request.form.get("from_team_logo")
    to_team_logo = request.form.get("to_team_logo")

    new_transfer = Transfer(
        player=player,
        from_team=from_team,
        to_team=to_team,
        date=date,
        fee=fee,
        image=image,
        from_team_logo=from_team_logo,
        to_team_logo=to_team_logo
    )
    db.session.add(new_transfer)
    db.session.commit()
    flash("New transfer added!", "success")

    return redirect(url_for("admin"))


@app.route("/add_favourite", methods=["POST"])
def add_favourite():
    if "user" not in session:
        flash("Please log in first", "warning")
        return redirect(url_for("login"))

    fav_type = request.form.get("fav_type")
    fav_name = request.form.get("fav_name")
    fav_api_id = request.form.get("fav_api_id")

    user = User.query.filter_by(username=session["user"]).first()

    exists = Favourite.query.filter_by(
        user_id=user.id,
        fav_type=fav_type,
        fav_api_id=fav_api_id
    ).first()

    if exists:
        flash(f"{fav_name} is already in your favourites!", "info")
    else:
        new_fav = Favourite(
            user_id=user.id,
            fav_type=fav_type,
            fav_name=fav_name,
            fav_api_id=fav_api_id
        )
        db.session.add(new_fav)
        db.session.commit()
        flash(f"{fav_name} added to favourites!", "success")

    return redirect(url_for("selection"))


@app.route("/admin/add_league", methods=["POST"])
def add_league():
    if "user" not in session or session["user"] != "admin":
        flash("You must be admin to add leagues", "danger")
        return redirect(url_for("login"))

    league_id = request.form.get("league_id", type=int)
    name = request.form.get("name")
    standings = request.form.get("standings") == "true"

    existing = League.query.get(league_id)
    if existing:
        flash("League with this ID already exists!", "warning")
    else:
        new_league = League(id=league_id, name=name, logo=f'https://media.api-sports.io/football/leagues/{league_id}.png', standings=standings)
        db.session.add(new_league)
        db.session.commit()
        flash(f"League {name} added successfully!", "success")

    return redirect(url_for("admin"))




from models import League

@app.route('/selection')
def selection():
    user_fav_ids = []
    if session.get("user"):
        user = User.query.filter_by(username=session["user"]).first()
        if user:
            user_fav_ids = [fav.fav_api_id for fav in user.favourites if fav.fav_type == "league"]

    leagues = League.query.all()
    return render_template("selection.html", leagues=leagues, user_fav_ids=user_fav_ids)

@app.route("/home")
def home():
    return render_template("home.html")


def findTop10(league_id):
    season = 2023
    url = f'{API_HOST}/standings?league={league_id}&season={season}'
    res = requests.get(url, headers=HEADERS)
    data = res.json()
    standings = data['response'][0]['league']['standings'][0]
    return standings[:10]

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        if League.query.count() == 0:
            initial_leagues = [
                {"id": 39, "name": "Premier League", "logo": "https://media.api-sports.io/football/leagues/39.png",
                 "standings": True},
                {"id": 61, "name": "Ligue 1", "logo": "https://media.api-sports.io/football/leagues/61.png",
                 "standings": True},
                {"id": 78, "name": "Bundesliga", "logo": "https://media.api-sports.io/football/leagues/78.png",
                 "standings": True},
                {"id": 135, "name": "Serie A", "logo": "https://media.api-sports.io/football/leagues/135.png",
                 "standings": True},
                {"id": 140, "name": "La Liga", "logo": "https://media.api-sports.io/football/leagues/140.png",
                 "standings": True},
                {"id": 2, "name": "Champions League", "logo": "https://media.api-sports.io/football/leagues/2.png",
                 "standings": True},
                {"id": 3, "name": "Europa League", "logo": "https://media.api-sports.io/football/leagues/3.png",
                 "standings": True},
            ]
            for league_data in initial_leagues:
                if not League.query.get(league_data["id"]):
                    db.session.add(League(**league_data))
            db.session.commit()

    app.run(host='0.0.0.0', port=5000, debug=True)

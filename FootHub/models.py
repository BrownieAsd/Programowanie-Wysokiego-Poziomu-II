from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    favourites = db.relationship('Favourite', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Transfer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player = db.Column(db.String(100), nullable=False)
    from_team = db.Column(db.String(100))
    to_team = db.Column(db.String(100))
    date = db.Column(db.String(50))
    fee = db.Column(db.String(50))
    image = db.Column(db.String(200))
    from_team_logo = db.Column(db.String(200))
    to_team_logo = db.Column(db.String(200))


class Favourite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    fav_type = db.Column(db.String(50), nullable=False)
    fav_name = db.Column(db.String(100), nullable=False)
    fav_api_id = db.Column(db.Integer, db.ForeignKey("league.id"), nullable=True)

class League(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    logo = db.Column(db.String(250))
    standings = db.Column(db.Boolean, default=True)

    favourites = db.relationship("Favourite", backref="league", lazy=True)

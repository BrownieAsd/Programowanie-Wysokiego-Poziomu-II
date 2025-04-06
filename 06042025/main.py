from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
users = {
    1: {"name": "Ala", "age": 22},
    2: {"name": "Bartek", "age": 25},
    3: {"name": "Celina", "age": 30}
}
tasks=[
    {"id" : 1, "title" : "Eat a pizza", "completed" : False},
    {"id" : 2, "title" : "Clean the house", "completed" :  False},
]

@app.route("/")
def hello():
    return render_template("hello.html")

@app.route("/users")
def get_users():
    return render_template("users.html", users=users)


@app.route("/about")
def about():
    return "This is a webpage with information about users and tasks ."

@app.route("/user/<int:user_id>")
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return f"{user.get('name')} is {user.get('age')} years old"
    else:
        return "User not found", 404

@app.route("/tasks", methods=['GET', 'POST', 'DELETE'])
def get_tasks():
    if request.method == "POST":
        title = request.form.get("title")
        if title:
            id = len(tasks) + 1
            tasks.append({"id": id, "title": title, "completed": False})
        return render_template("tasks.html", tasks=tasks)
    return render_template("tasks.html", tasks=tasks)

@app.route("/tasks/<int:task_id>/completed", methods=['POST'])
def completed(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
    return render_template("tasks.html", tasks=tasks)

@app.route("/tasks/<int:task_id>/delete", methods=['POST'])
def delete(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
    return render_template("tasks.html", tasks=tasks)


if __name__ == "__main__":
    app.run(debug=True)

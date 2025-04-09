from flask import Flask, render_template

app = Flask(__name__)

users = {
    1: {"name": "Ala", "age": 22},
    2: {"name": "Bartek", "age": 25},
    3: {"name": "Celina", "age": 30}
}


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return "To jest podstrona 'O nas'."


@app.route("/user/<int:user_id>")
def user_description(user_id: int):
    user = users.get(user_id)
    if user:
        return f"{user['name']} ma {user['age']} lat"
    else:
        return "Użytkownik nie istnieje"


@app.route("/users")
def users_listing():
    return render_template('users.html', users=users)


if __name__ == "__main__":
    app.run(debug=True)

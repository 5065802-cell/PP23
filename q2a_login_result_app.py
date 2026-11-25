from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    user = request.form.get("username")
    return render_template("result.html", username=user)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def handle():
    if request.method == "POST":
        val = request.form.get("value")
        return f"<h3>Submitted Value: {val}</h3><p>Request Method: {request.method}</p>"
    return '''
    <form method="POST">
      Enter Value: <input type="text" name="value" required>
      <button type="submit">Submit</button>
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)

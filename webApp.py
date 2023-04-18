from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    text_input = request.form["text-input"]
    file_input = request.files["file-input"]
    # process the text and file data here
    result = "Processed data"
    return result

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/members')
def members():
    return render_template("underdev.html", title="Members")

@app.route('/gallery')
def gallery():
    return render_template("underdev.html", title="Gallery")

@app.route('/support')
def support():
    return render_template("underdev.html", title="Support")

if __name__ == "__main__":
    app.run(port=8080, debug=True)
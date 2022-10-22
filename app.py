from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('resume.html',
    style_path = url_for('static', filename = 'style.css'))

if __name__ == "__main__":
    app.run(debug=True)
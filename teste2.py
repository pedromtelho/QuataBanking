from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello"

if __name__ == "__main__":
    app.run(debug=True)
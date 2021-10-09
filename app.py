from flask import Flask, render_template, request, url_for, flash, redirect, Request
import yagmail
import utils
import os


app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__=='__main__':
    app.run(debug=True, port=8080)
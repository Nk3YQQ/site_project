from flask import Flask, requiest, render_template

app = Flask(__name__)


@app.post('/users')
def users_post():
    pass

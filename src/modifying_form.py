from flask import Flask, render_template, request, redirect
from classes import UserRepository, User
from utils import validate

app = Flask(__name__)


@app.post('/users')
def users_post():
    repo = UserRepository()
    user_data = request.form.to_dict()
    user = User(**user_data)
    errors = validate(user)
    if errors:
        return render_template(
            'new.html',
            user=user,
            errors=errors
        ), 422
    repo.save(user)
    return redirect('/users', code=302)


@app.route('/users/new')
def users_new():
    user = User(
        name='',
        email='',
        password='',
        passwordConfirmation=''
    )
    errors = {}

    return render_template(
        'new.html',
        user=user,
        errors=errors
    )


if __name__ == '__main__':
    app.run(port=5000, debug=True)

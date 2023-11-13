def validate(user):
    errors = {}

    if not user.name:
        errors['name'] = 'Не может быть пустым'

    if not user.email:
        errors['email'] = 'Не может быть пустым'
    elif '@' not in user.email or '.' not in user.email:
        errors['email'] = 'Некорректный формат email'

    if not user.password:
        errors['password'] = 'Не может быть пустым'

    if len(user.password) <= 5:
        errors['password'] = 'Слишком короткий пароль'

    if user.password != user.passwordConfirmation:
        errors['passwordConfirmation'] = 'Пароли не совпадают'

    return errors

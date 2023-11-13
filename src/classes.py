import json


class User:
    def __init__(self, name, email, password, passwordConfirmation):
        self.name = name
        self.email = email
        self.password = password
        self.passwordConfirmation = passwordConfirmation


class UserRepository:
    def __init__(self, file_path='../data/users.json'):
        self.file_path = file_path
        self.users = self.content()

    def content(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            return []

    def save_users(self):
        with open(self.file_path, 'w', encoding="utf-8") as file:
            json.dump(self.users, file, ensure_ascii=False, indent=4)

    def save(self, user):
        existing_usernames = [existing_user['Имя пользователя'] for existing_user in self.users]
        if user.name in existing_usernames:
            print(f"User with username '{user.name}' already exists.")
        else:
            self.users.append({
                'Имя пользователя': user.name,
                'Email': user.email,
                'Пароль': user.password
            })
        self.save_users()

    def find(self, name):
        for user in self.users:
            if user['Имя пользователя'] == name:
                return user

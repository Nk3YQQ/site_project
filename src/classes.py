import json


class UserRepository:
    def __init__(self, file_path='data/users.json'):
        self.file_path = file_path

    def content(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save(self, user):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            users = json.load(file)
            update_users = users.append(user)
            json.dump(update_users, file)

    def find(self, user_id):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            users = json.load(file)
            for user in users:
                if user['id'] == user_id:
                    return user

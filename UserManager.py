import json

class UserManager:
    def __init__(self, filename="users.json"):
        self.filename = filename
        self.users = self.load_users()

    def load_users(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_users(self):
        with open(self.filename, "w") as file:
            json.dump(self.users, file, indent=4)

    def register_user(self, username, password):
        if username in self.users:
            return False, "Bu kullanıcı adı zaten var."
        self.users[username] = password
        self.save_users()
        return True, f"Kullanıcı başarıyla kaydedildi: {username}"

    def login_user(self, username, password):
        if username in self.users and self.users[username] == password:
            return True, f"Giriş başarılı: Hoş geldiniz, {username}!"
        return False, "Geçersiz kullanıcı adı veya şifre."

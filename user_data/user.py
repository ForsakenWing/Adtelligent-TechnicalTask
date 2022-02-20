from user_data import generate_login, generate_email, generate_password


class User:

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    @staticmethod
    def create_random_user():
        login = generate_login()
        password = generate_password()
        email = generate_email()
        return User(login, password, email)

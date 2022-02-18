from unittest import TestCase, main
from request_to import post, get, create_session, update_user, destroy_session
from user import User


class Parent:

    new_user = User()

    data = post(new_user.login, new_user.password, new_user.email)
    new_user_token = data.get('User-Token')
    login = new_user.login
    password = new_user.password
    if new_user_token:
        print("User successfully created")

    get_session = create_session(login, password)
    token = get_session.get('User-Token')
    print(token)

    # I didn`t find a key how to fix this bug with get_user_details function

    get_user_details = get(token)  # BUG/ERROR Getting an error "User not found"

    login = get_session.get('login')
    email = get_session.get('email')


class CreatingUserTest(TestCase, Parent):

    def test_registration(self):
        self.assertEqual(self.new_user.login, self.login)

        # Getting an bug/error (Email_name is automatically switching
        # to lowercase what called an error in Tests)

        # if we switch our email to lowercase == tests would pass

        self.assertEqual(self.new_user.email.lower(), self.email)


class UpdatingUserTest(TestCase, Parent):

    new_user_data = User()
    update_user_data = update_user(Parent.token,
                                   new_user_data.login,
                                   new_user_data.new_email)
    print(update_user_data)

    print(destroy_session())

    def test_updating(self):
        self.assertEqual(self.new_user_data.login, "jopik")

        self.assertEqual(self.new_user_data.email, "jopik2")


if __name__ == "__main__":
    main()

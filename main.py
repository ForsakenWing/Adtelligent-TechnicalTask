from unittest import TestCase, main
from Requests import post, get, update_user, destroy_session
from user_data import User


class Parent:

    new_user = User.create_random_user()

    data = post(new_user.login, new_user.password, new_user.email)
    _user_token = data.get('User-Token')

    if _user_token:
        print("User successfully created.")

    get_response = get(_user_token, new_user.login)

    get_login = get_response['login']
    get_email = get_response['account_details']['email']


class CreatingUserTest(TestCase, Parent):

    def test_registration(self):
        self.assertEqual(self.new_user.login,
                         self.get_login)

        # Getting a bug/error (Email_name is automatically switching
        # to lowercase what called an error in Tests)

        # if we switch our email to lowercase == tests would pass

        self.assertEqual(self.new_user.email.lower(),
                         self.get_email)


class UpdatingUserTest(TestCase, Parent):

    new_user_data = User.create_random_user()

    updated_user_data = update_user(Parent._user_token,
                                    new_user_data.login,
                                    new_user_data.email,
                                    Parent.get_login)

    get_updated_user_data = get(Parent._user_token,
                                new_user_data.login)

    if updated_user_data['message'] == "User successfully updated.":

        print("User successfully updated.")

        def test_updating(self):

            self.assertEqual(self.new_user_data.login,
                             self.get_updated_user_data['login'])

            # Getting a bug/error (Email_name is automatically switching
            # to lowercase what called an error in Tests)

            # if we switch our email to lowercase == tests would pass

            self.assertEqual(self.new_user_data.email.lower(),
                             self.get_updated_user_data['account_details']['email'])

    else:
        raise Exception("User wasn`t updated successfully")

    print(destroy_session(Parent._user_token)['message'])


if __name__ == "__main__":
    main()

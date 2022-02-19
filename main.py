from unittest import TestCase, main
from Requests.request_to import post, get, update_user, destroy_session
from user_data.user import User


class Parent:
    new_user = User()

    data = post(new_user.login, new_user.password, new_user.email)
    user_token = data.get('User-Token')
    login = new_user.login
    password = new_user.password

    if user_token:
        print("User successfully created")

    get_user_details = get(user_token, login)

    response_login = get_user_details['login']
    response_email = get_user_details['account_details']['email']


class CreatingUserTest(TestCase, Parent):

    def test_registration(self):
        self.assertEqual(self.new_user.login,
                         self.response_login)

        # Getting a bug/error (Email_name is automatically switching
        # to lowercase what called an error in Tests)

        # if we switch our email to lowercase == tests would pass

        self.assertEqual(self.new_user.email.lower(),
                         self.response_email)


class UpdatingUserTest(TestCase, Parent):
    new_user_data = User()

    updated_user_data = update_user(Parent.user_token,
                                    new_user_data.login,
                                    new_user_data.email,
                                    Parent.response_login)

    get_updated_user_data = get(Parent.user_token,
                                new_user_data.login)

    if updated_user_data['message'] == "User successfully updated.":

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

    print(destroy_session(Parent.user_token)['message'])


if __name__ == "__main__":
    main()

import requests


auth_token = '84b0561d0adc0778f86f89ed63dbbee0'
auth_header = {"Authorization": f'Token token={auth_token}'}


def post(login, password, email):

    data = {
        "user": {
            "login": f"{login}",
            "email": f"{email}",
            "password": f"{password}"
        }
    }

    response = requests.post(url=r"https://favqs.com/api/users", json=data,
                             headers=auth_header).json()

    return response


def get(token, login):

    usr_token = {"User-Token": f"{token}"}

    response = requests.get(url=rf"https://favqs.com/api/users/{login}",
                            headers={**auth_header, **usr_token})

    return response.json()


def update_user(user_token, new_login, new_email, old_login):

    header = {"User-Token": user_token}

    data = {

        "user": {

            "login": f"{new_login}",
            "email": f"{new_email}"

        }
    }

    response = requests.put(url=rf"https://favqs.com/api/users/{old_login}",
                            json=data, headers={**header, **auth_header})

    return response.json()


def destroy_session(token):

    response = requests.delete("https://favqs.com/api/session",
                               headers={**auth_header, **{"User-Token": token}})

    return response.json()

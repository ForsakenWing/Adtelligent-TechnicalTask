import requests
token = '84b0561d0adc0778f86f89ed63dbbee0'
auth_header = {"Authorization": f'Token token={token}'}


def post(login, password, email):
    data = {
        "user": {
            "login": f"{login}",
            "email": f"{email}",
            "password": f"{password}"
        }
    }

    response = requests.post(url=r"https://favqs.com/api/users", json=data,
                             headers=auth_header)

    return response.json()


def get(token):
    header = {"User-Token": f"{token}"}

    response = requests.get(url=r"https://favqs.com/api/users/:login",
                            headers={**auth_header, **header})

    return response.json()


def create_session(login, password):
    data = {
        "user": {
            "login": f"{login}",
            "password": f"{password}"
        }
    }

    response = requests.post(r"https://favqs.com/api/session", json=data,
                             headers=auth_header)

    return response.json()


def update_user(user_token, new_login, new_email):
    header = {"User-Token": f"{user_token}",
              "Authorization": f'Token token={token}'}

    data = {

        "user": {

            "login": f"{new_login}",
            "email": f"{new_email}"

        }
    }

    response = requests.get(url=r"https://favqs.com/api/users/:login",
                            json=data, headers=header)

    return response.json()


def destroy_session():

    response = requests.delete("https://favqs.com/api/session", headers=auth_header)

    return response.json()
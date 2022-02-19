from random import randint
from secrets import choice
from string import ascii_lowercase as as_low, digits as dig
from string import ascii_letters as as_let, punctuation as punc


class User:

    def __init__(self):

        self.login = self.new_login()
        self.password = self.new_password()
        self.email = self.new_email()

    @staticmethod
    def new_login():

        login_length = randint(1, 20)

        return "".join((choice([*as_low, *dig, "_"]) for _ in range(login_length)))

    @staticmethod
    def new_password():

        password_length = randint(5, 120)

        return "".join((choice([*as_let, *dig, *punc]) for _ in range(password_length)))

    @staticmethod
    def new_email():

        email_length = [randint(1, 63), randint(1, 63)]
        recipient_name, domain_name = email_length
        # For some reasons it doesnt work...
        # punc_for_recipient = "! # $ % & ‘ * + – / = ?  ^ _ ` . { | } ~"
        default_top_lvl_domains = [".com", ".ru", ".uk", ".ua"]

        return f"{choice([*as_let, *dig])}" \
               f"{''.join((choice([*as_let, *dig]) for _ in range(recipient_name - 1)))}@" \
               f"{choice([*as_let, *dig])}" \
               f"{''.join((choice([*as_let, *dig, '-']) for _ in range(domain_name - 1)))}" \
               f"{choice(default_top_lvl_domains)}"



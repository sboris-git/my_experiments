import re

def user():

    email = input('type the email: ')
    username = email.split('@')[0]
    print(username)


user()

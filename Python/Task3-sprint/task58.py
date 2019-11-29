import re

def user():
    email = input('type the email: ')
    domain = email.split('@')[1]
    domain_name = domain.split('.')[0]
    print(domain_name)


user()
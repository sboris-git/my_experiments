def user():

    email = input('type the email: ')
    username = email.split('@')[0]
    return username


print(user())

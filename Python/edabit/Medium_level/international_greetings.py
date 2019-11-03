GUEST_LIST = {
    "Randy": "Germany",
    "Karla": "France",
    "Wendy": "Japan",
    "Norman": "England",
    "Sam": "Argentina"
}


def greeting(name):
    '''Suppose you have a guest list of students and the country they are from,
    stored as key-value pairs in a dictionary.
    A function that takes in a name and returns a name tag, that should read:
    "Hi! I'm [name], and I'm from [country]."
    If the name is not in the dictionary, return:
    "Hi! I'm a guest."
    Example:
        print(greeting("Sam") == "Hi! I'm Sam, and I'm from Argentina.")
        print(greeting("Monti") == "Hi! I'm a guest.")
    Ref: edabit.com
    '''
    # greet = f"Hi! I'm {name}, and I'm from {GUEST_LIST[name]}."\
    #     if name in GUEST_LIST.keys() else "Hi! I'm a guest."
    greet = "Hi! I'm {}, and I'm from {}.".format(name, GUEST_LIST[name]) \
        if name in GUEST_LIST.keys() else "Hi! I'm a guest."

    return greet


# Examples
print(greeting("Randy") == "Hi! I'm Randy, and I'm from Germany.")
print(greeting("Sam") == "Hi! I'm Sam, and I'm from Argentina.")
print(greeting("Monti") == "Hi! I'm a guest.")

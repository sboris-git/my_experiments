import re
from collection import list_to_str


def check(text):

    valid = None
    tmp_list = []
    if 6 <= len(text) <= 12:
        tmp_list.append(bool(re.search("[a-z]", text)))
        tmp_list.append(bool(re.search("[A-Z]", text)))
        tmp_list.append(bool(re.search("[0-9]", text)))
        tmp_list.append(bool(re.search("[$#@]", text)))
    if tmp_list.count(True) >= 4:
        valid = text

    return valid


def validation(pswd):

    valid_pswd = []
    if isinstance(pswd, list):
        for passwrd in pswd:
            if check(passwrd) is not None:
                valid_pswd.append(passwrd)
    else:
        valid_pswd.append(valid_pswd)

    return print(list_to_str(valid_pswd))  # ToDo , ','


pass_list = ['ABd1234@1', 'a F1#', '2w3E*', '2We3345']
validation(pass_list)
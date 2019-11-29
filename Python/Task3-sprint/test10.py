from collection import list_to_str

def wsd_text(text):

    return print(list_to_str(sorted(set(text.split())),' '))

wsd_text('hello world and practice makes perfect and hello world again')
import re


def space_separated():
    text = input('Type a text: ')
    pattern = re.compile(r'\d+')
    matches = pattern.findall(text)

    return matches
    # pattern = re.compile(r'(\d+)')
    # matches = pattern.finditer(text)
    # return print([match.group(0) for match in matches])


# text = '2 cats and 30 dogs.'
print(space_separated())

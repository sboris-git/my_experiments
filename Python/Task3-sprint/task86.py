def sentence():
    '''Question 86
    Please write a program to generate all sentences where subject is in ["I", "You"] and
    verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].'''

    subjects = ["I", "You"]
    verbs = ["Play", "Love"]
    objects = ["Hockey", "Football"]
    full = []
    for sub in subjects:
        sent = []
        for verb in verbs:
            subj_verb = []
            for obj in objects:
                subj_verb.append([sub, verb, obj])
            sent.append(subj_verb)
        full.append(sent)

    return full


print(sentence())
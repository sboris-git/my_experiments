from random import shuffle


def shuffle_lst(lst):
    '''Question 84
    Please write a program to shuffle and print the list [3,6,7,8].'''

    shuffle(lst)
    return lst

if __name__ == '__main__':
    lst = [3, 6, 7, 8]
    print(shuffle_lst(lst))





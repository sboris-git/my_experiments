def sum_two_int_str(str1, str2):
    str_x = str1 if len(str1) > len(str2) else str2
    return str_x


print(sum_two_int_str('233', '11'))
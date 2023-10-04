#!/usr/bin/python3
def remove_char_at(str, n):
    str1 = [None] * (len(str) - 1)
    j = 0
    for i in range(len(str)):
        if (i != n):
            str1[j] = str[i]
            j += 1
    return (str1)

import os
global final

def save_default_oper(Fin_sum):
    print(Fin_sum)
    f = open('file.txt', 'w')
    f.write(str(Fin_sum))
    f.close()

def save_another_op(Fin_sum):
    Fin_sum = ''.join(Fin_sum)
    Fin_sum = int(str(Fin_sum), 2)
    print(Fin_sum)
    f = open('file.txt', 'w')
    f.write(str(Fin_sum))
    f.close()

f = open('file.txt', 'r')
string_from_file = f.readline()
f.close()

if "+" in string_from_file:
    split_string = string_from_file.split("+")
    Fin_sum = int(split_string[0]) + int(split_string[1])
    save_default_oper(Fin_sum)
if "-" in string_from_file:
    split_string = string_from_file.split("-")
    Fin_sum = int(split_string[0]) - int(split_string[1])
    save_default_oper(Fin_sum)
if "*" in string_from_file:
    split_string = string_from_file.split("*")
    Fin_sum = int(split_string[0]) * int(split_string[1])
    save_default_oper(Fin_sum)
if "/" in string_from_file:
    split_string = string_from_file.split("/")
    Fin_sum = int(split_string[0]) // int(split_string[1])
    save_default_oper(Fin_sum)

if "^" in string_from_file:
    split_string = string_from_file.split("^")
    b1 = list(str(format(int(split_string[0]), 'b')))
    b2 = list(str(format(int(split_string[1]), 'b')))
    len_b1 = len(b1) - 1
    len_b2 = len(b2) - 1
    if len_b1 >= len_b2:
        while len_b1 != len_b2:
            final = b1
            if len_b2 <= -1:
                final[len_b1] = b2[len_b1]
                len_b1 = len_b1 - 1
            else:
                if b1[len_b1] == '0' and b2[len_b2] == '0':
                    final[len_b1] = '0'
                if b1[len_b1] == '1' and b2[len_b2] == '1':
                    final[len_b1] = '0'
                else:
                    final[len_b2] = '1'
                len_b1 = len_b1 - 1
                len_b2 = len_b2 - 1
    else:
        final = b2
        while len_b2 != len_b1:
            if len_b1 <= -1:
                final[len_b2] = b2[len_b2]
                len_b2 = len_b2 - 1
                print("СМЕЩЕНИЕ")
            else:
                print(b2[len_b2], b1[len_b1])
                if b2[len_b2] == '0' and b1[len_b1] == '0':
                    final[len_b2] = '0'
                elif b2[len_b2] == '1' and b1[len_b1] == '1':
                    final[len_b2] = '0'
                else:
                    final[len_b2] = '1'
                print(final[len_b2])
                len_b1 = len_b1 - 1
                len_b2 = len_b2 - 1
    Fin_sum = final
    save_another_op(Fin_sum)
if "|" in string_from_file:
    split_string = string_from_file.split("|")
    a1 = int(format(int(split_string[0]), 'b'))
    a2 = int(format(int(split_string[1]), 'b'))
    b1 = list(format(a1, 'b'))
    b2 = list(format(a2, 'b'))
    len_b1 = len(b1) - 1
    len_b2 = len(b2) - 1
    if len_b1 >= len_b2:
        final = b1
        while len_b1 != len_b2:
            if len_b2 <= -1:
                final[len_b1] = b2[len_b1]
                len_b1 = len_b1 - 1
            else:
                if b1[len_b1] == '0' and b2[len_b2] == '0':
                    final[len_b1] = '0'
                else:
                    final[len_b2] = '1'
                len_b1 = len_b1 - 1
                len_b2 = len_b2 - 1
    else:
        final = b2
        while len_b2 != len_b1:
            if len_b1 <= -1:
                final[len_b2] = b1[len_b2]
                len_b2 = len_b2 - 1
            else:
                if b2[len_b2] == '0' and b1[len_b1] == '0':
                    final[len_b2] = '0'
                else:
                    final[len_b2] = '1'
                len_b1 = len_b1 - 1
                len_b2 = len_b2 - 1
    Fin_sum = final
    save_another_op(Fin_sum)
def ASCII_string(num, count=10):
    ASCII_str = ''
    if count == 1:
        return (str(num) + "-" + chr(num))
    else:
        ASCII_str = str(num) + " " + chr(num) + ", " + ASCII_string(num + 1, count - 1)
        return ASCII_str


def calcul(num_begin, num_end):
    if num_begin > num_end - 10:
        print(ASCII_string(num_begin, (abs(num_end - num_begin) + 1)))
    else:
        print(ASCII_string(num_begin))
        calcul(num_begin + 10, num_end)


calcul(32, 127)

def NumberValues(BinaryToOctal):
    BinaryToOctal["000"] = '0'
    BinaryToOctal["001"] = '1'
    BinaryToOctal["010"] = '2'
    BinaryToOctal["011"] = '3'
    BinaryToOctal["100"] = '4'
    BinaryToOctal["101"] = '5'
    BinaryToOctal["110"] = '6'
    BinaryToOctal["111"] = '7'


def BinToOct(bin):
    l = len(bin)
    t = -1
    if "." in bin:
        t = bin.index(".")
        len_left = t
    else:
        len_left = l
    for i in range(1, (3 - len_left % 3) % 3+1):

        bin = '0' + bin
    if (t != -1):
        len_right = l - len_left - 1
        for i in range(1, (3 - len_right % 3) % 3+1):
            bin = '0' + bin
    BinaryToOctal = {}
    NumberValues(BinaryToOctal)
    i = 0
    oct = ""
    while(True):
        oct += BinaryToOctal[bin[i:i + 3]]
        i += 3
        if(i == len(bin)):
            break
        if (bin[i] == '.'):
            oct += '.'
            i += 1
    return oct

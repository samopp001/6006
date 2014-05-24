__numbers = {0:"zero",
           1:"one",
           2:"two",
           3:"three",
           4:"four",
           5:"five",
           6:"six",
           7:"seven",
           8:"eight",
           9:"nine",
           10:"ten",
           11:"eleven",
           12:"twelve",
           13:"thirteen",
           14:"fourteen",
           15:"fifteen",
           16:"sixteen",
           17:"seventeen",
           18:"eighteen",
           19:"nineteen",
           20:"twenty",
           30:"thirty",
           40:"forty",
           50:"fifty",
           60:"sixty",
           70:"seventy",
           80:"eighty",
           90:"ninety",
           100:"hundred",
           1000:"thousand"}

def num2str(i):
    if i < 0:
        return "negative" + " " + num2str(-i)
    elif i<20:
        return __numbers[i]
    elif i<100:
        num = i / 10
        rem = i % 10
        return __numbers[num*10] + ((" "+num2str(rem)) if (rem > 0) else "")
    elif i<1000:
        num = i / 100
        rem = i % 100
        return num2str(num) + " " + __numbers[100] + ((" "+num2str(rem)) if (rem > 0) else "")
    else:
        num = i / 1000
        rem = i % 1000
        return num2str(num) + " " + __numbers[1000] + ((" "+num2str(rem)) if (rem > 0) else "")
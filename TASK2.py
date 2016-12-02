m = int(input('Your number ?:'))  # user input of the number
n = 0

def fact(m):#calculate factorial of the number

    if m < 0:
        print('Sorry but negative numbers dont have factorials')
    else:
        i = 2
        temp = 1
        while i <= m :
            temp*= i
            i += 1
        return temp

def trailingZ(m):#calculate the trailing zeros in the factorial

    f = fact(m)
    f = str(f)
    r = f[::-1]
    rNum = int(r)
    rNum = str(rNum)

    return(len(r) - len(rNum))

if m < 0:
    pass
else:
    print('The factorial of your number is %s and it has %s trailing zeros.' % (fact(m), trailingZ(m)))



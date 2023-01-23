import string
a = string.digits
while True:
    print('How many pencils would you like to use:')
    number = input()
    if not number.isdigit() and number != '0':
        print('The number of pencils should be numeric')
    elif number == '0':
        print('The number of pencils should be positive')
    else:
        break
print('Who will be the first (John, Jack):')
while True:
    name = input()
    name1 = 'Jack'
    name2 = "John"
    if name != name1 and name != name2:
        print("Choose between 'John' and 'Jack'")
    else:
        number = int(number)
        print('|'*number)
        break
while True:
    if name == 'Jack':
        print("{}'s turn:".format(name1),sep="")
        if number % 4 == 0:
            digit = 3
            print(digit)
        elif number % 4 == 3:
            digit = 2
            print(digit)
        elif number % 4 == 2:
            digit = 1
            print(digit)
        else:
            digit = 1
            print(digit)
        while True:
            if number == 1:
                print("{} won!".format(name2))
                break
            else:
                break
        if number != 1:
            print('|' * (number - digit))
            number = number-digit
        else:
            break
        name = name2
    else:
        print("{}'s turn:".format(name2), sep="")
        while True:
            c = input()
            if not c.isdigit():
                print("Possible values: '1', '2' or '3'")
            elif int(c) != 1 and int(c) != 2 and int(c) != 3:
                print("Possible values: '1', '2' or '3'")
            elif (int(c)) > number:
                print('Too many pencils were taken')
            elif (int(c)) == number:
                print("{} won!".format(name1))
                break
            else:
                break
        if (int(c)) < number and (int(c)) !=0:
            print('|' * (number - (int(c))))
            number = number - (int(c))
        else:
            break
        name = name1

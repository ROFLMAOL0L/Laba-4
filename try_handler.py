def float_input(n):
    if isinstance(n, str):
        try:
            return float(input(n))
        except ValueError:
            print('invalid input, please try again')
            return float_input(n)
    else:
        print('ErrorInCode: n is not a str (try_handler)')

def int_input(n):
    if isinstance(n, str):
        try:
            return int(input(n))
        except ValueError:
            print('invalid input, please try again')
            return int_input(n)
    else:
        print('ErrorInCode: n is not a str (try_handler)')

def choice2_input(n):
    if isinstance(n, str):
        a = input(n)
        if a == '1' or a == '2':
            return (int(a))
        else:
            print('invalid input, please try again')
            return choose2_input(n)
    else:
        print('ErrorInCode: n is not a str (try_handler)')

def choice3_input(n):
    if isinstance(n, str):
        a = input(n)
        if a == '1' or a == '2' or a == '3':
            return (int(a))
        else:
            print('invalid input, please try again')
            return choose3_input(n)
    else:
        print('ErrorInCode: n is not a str (try_handler)')

def choice4_input(n):
    if isinstance(n, str):
        a = input(n)
        if a == '1' or a == '2' or a == '3' or a == '4':
            return (int(a))
        else:
            print('invalid input, please try again')
            return choose4_input(n)
    else:
        print('ErrorInCode: n is not a str (try_handler)')

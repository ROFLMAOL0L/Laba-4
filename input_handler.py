import math
from excel_handler import deix
from time import time
split_operators = ['^', '/', '*', '+']
allowed_string_patterns = ['log', 'sin', 'cos', 'lg', 'ln', 'x']
# Правила записи функций: log(основание, значение), sin(x), cos(x), lg(x), ln(x), x
# x ** (1 + x), x + (1 + 123), x / (1 + 1),\
# To do 1/3 + 1/3 + 1/3 = 1.0 we can do (1/3 * 3 + 1/3 * 3 + 1/3 * 3) / 3
# BUG x**82 + cos(x**9) + log(2, x**2 + 9) + 100   or    cos(x**9) + log(2, 5**2 + 9) + 100


def handle_input(func, name2, x_range_input=(-10, 10), x_scaling_input=1):
    handle_input_start_time = time()
    func = func.lower()
    func = func.replace(' ', '')
    func = func.replace('**', '^')
    func = func.replace('log', 'lo')
    func = func.replace('-', '+-')
    if 'x' not in func:
        return calculate(func)
    else:
        y_range = []
        x_range = []
        x = x_range_input[0]
        while x < x_range_input[1]:
            x_range.append(x)
            x += x_scaling_input
        for x in x_range:
            y = calculate(func.replace('x', str(x)))
            if y == 'Error':
                return None
            y_range.append(float(y))
            # print(str(y) + ')')
        print('Обработка формулы заняла ', time() - handle_input_start_time, 'секунд.')
        deix(x_range, y_range, func, name2)


def look_for_brackets(brackets_string):
    function1 = brackets_string
    i = 0
    while i < len(function1):
        if function1[i] == '(':
            if function1[i - 1] not in ['g', 'n', 's', 'o']:
                j = i
                while j < len(function1) and function1[j] != ')':
                    j += 1
                if j == len(function1):
                    print('Не найдена закрывающая скобка.')
                    return None
                function1 = function1[0:i] + calculate(function1[i + 1:j]) + function1[j + 1:]
        i += 1
    return function1


def calculate_hard_functions(hard_string):
    # (print(hard_string)
    function2 = hard_string
    new_string1 = ''
    l_s = len(hard_string)
    i_i = 0
    last_stop = 0
    print('NASDKFJLSKDKGJ:', hard_string)
    print('No fucking way............ ', i_i)
    while i_i < l_s:
        letter_of_string = function2[i_i]
        print('AXAXA_____ lol:', letter_of_string, hard_string, i_i, last_stop)
        if not letter_of_string.isnumeric():
            if letter_of_string == 'l':
                if function2[i_i+1] == 'o':
                    j = i_i + 2
                    while j < l_s and function2[j] != ')':
                        print('DOLBOEB: ', function2[j])
                        j += 1
                    insides = function2[i_i+3:j].split(',')
                    print('Insides of log are: ', insides, 'Index is: ', function2[j])
                    base = float(calculate(insides[0]))
                    value = float(calculate(insides[1]))
                    new_string1 += str(math.log(abs(value), abs(base)))
                    i_i += j + 2
                    last_stop = j + 2
                elif function2[i_i+1] == 'n':
                    j = i_i + 2
                    while j < l_s and function2[j] != ')':
                        j += 1
                    insides = function2[i_i+3:j-1]
                    # print('Insides of ln are: ', insides)
                    new_string1 += str(math.log(float(calculate(insides))))
                    i_i += j + 2
                    last_stop = j + 1
                elif function2[i_i+1] == 'g':
                    j = i_i + 2
                    while j < l_s and function2[j] != ')':
                        j += 1
                    insides = function2[i_i+3:j-1]
                    # print('Insides of lg are: ', insides)
                    new_string1 += str(math.log(float(calculate(insides)), 10))
                    i_i += j + 2
                    last_stop = j + 1
            elif letter_of_string == 's':
                j = i_i + 3
                while j < l_s and function2[j] != ')':
                    j += 1
                insides = function2[i_i + 4:j]
                print('Insides of sin are: ', insides)
                new_string1 += str(math.sin(float(calculate(insides))))
                i_i += j + 2
                last_stop = j + 1
            elif letter_of_string == 'c':
                j = i_i + 3
                while j < l_s and function2[j] != ')':
                    j += 1
                insides = function2[i_i + 4:j]
                print('Insides of sin are: ', insides)
                new_string1 += str(math.cos(float(calculate(insides))))
                i_i += j + 2
                last_stop = j + 1
            elif letter_of_string in split_operators:
                new_string1 += function2[last_stop:i_i+1]
                last_stop = i_i+1
        i_i += 1
    new_string1 += function2[last_stop:]
    i_i = 0
    print('OSIDHJF:KSJDJISDGJKFLJKLSDGJKLGSDJKLGSIJGSD:', new_string1)
    return new_string1


def split_into_mass(func_split):
    new_mas = []
    last_stop = 0
    for i, letter_of_sting in enumerate(func_split):
        # print(letter_of_sting)
        if letter_of_sting in split_operators:
            # print(func_split[last_stop:i], func_split[i])
            new_mas.append(func_split[last_stop:i])
            new_mas.append(func_split[i])
            last_stop = i+1
    new_mas.append(func_split[last_stop:])
    # print(new_mas)
    return new_mas


def calculate_numbers(num1, num2, operation_index):
    if not num1.isnumeric():
        num1 = calculate(num1)
    if not num2.isnumeric():
        num2 = calculate(num2)
    print(num1, split_operators[operation_index], num2)
    if operation_index == 0:
        return float(num1) ** float(num2)
    if operation_index == 1:
        return float(num1) / float(num2)
    if operation_index == 2:
        return float(num1) * float(num2)
    if operation_index == 3:
        return float(num1) + float(num2)
    if operation_index == 4:
        return float(num1) - float(num2)


def shrink(shrink_string):
    global tabulee
    new_string = shrink_string
    # ans_mas = []        # This line is commented cause pycharm says ans_mas is not used !!!
    # print('lol', new_string)
    while len(new_string) != 1:
        # print('what?', new_string)
        j = 0
        # print(new_string)
        while j < len(split_operators):
            operator_check = split_operators[j]
            i = len(new_string) - 1
            while i >= 0:
                if operator_check == new_string[i]:
                    # print('first lol', new_string[0:i - 1])
                    # print('Calc lol', calculate_numbers(new_string[i - 1], new_string[i + 1], j))
                    # print('end lol', new_string[i + 1:])
                    ans_mas = new_string[0:i - 1] + [str(calculate_numbers(new_string[i - 1], new_string[i + 1], j))]
                    ans_mas += new_string[i + 2:]
                    new_string = ans_mas
                    # ans_mas = []       # That one as well
                    i = len(new_string)
                i -= 1
            j += 1
    return str(new_string[0])


# (1 + 2) + ((1 + 2) + 3)
def calculate(func):
    print('Nigga why u play with ME?????????', func)
    if func.isnumeric():
        return func
    print('Hard calc')
    function = calculate_hard_functions(func)
    print('Look for brackets')
    new_string1 = look_for_brackets(function)
    if function is None:
        return 'Error'

    new_string1 = split_into_mass(new_string1)
    # By the end we have a string '1+23^7*123+4' into ['1', '+', '23', '^', '7', '^', '123', '+', '4']
    # Actual handling the calculations
    return shrink(new_string1)

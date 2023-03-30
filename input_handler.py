import math
from excel_handler import deix
split_operators = ['^', '*', '/', '+', '-']
allowed_string_patterns = ['log', 'sin', 'cos', 'lg', 'ln', 'x']

# Правила записи функций: log(основание, значение), sin(x), cos(x), lg(x), ln(x), x
# x ** (1 + x), x + (1 + 123), x / (1 + 1),

def handle_input(func):
    func.lower()
    func = func.replace(' ', '')
    func = func.replace('**', '^')
    if 'x' not in func:
        return calculate(func)
    else:
        y_range = []
        x_range = [x for x in range(0, 10)]
        for x in range(0, len(x_range)):
            y_range.append(calculate(func.replace('x', str(x))))
        deix(x_range, y_range, func)




# (1 + 2) + ((1 + 2) + 3)
def calculate(func):
    function = func
    i = 0
    while i < len(function):
        if function[i] == '(':
            if i > 0 and function[i - 1] not in ['g', 'n', 's']:
                j = i
                while j < len(function) and function[j] != ')':
                    j += 1
                function = function[0:i] + calculate(function[i + 1:j] + '|') + function[j+1:]
        i += 1
    new_string = []
    i = 0
    while i < len(function):

        # Check if operator
        if function[i] in split_operators:
            new_string.append(function[i])

        # Do if not operator
        else:
            # Check if hard function
            if i + 3 < len(function):
                # Check if log, sin, cos
                if function[i:i + 3] in allowed_string_patterns:
                    j = i + 4

                    # Check if hard function with hard insides log((x + 1) + 2) and for usual log(x + 1)
                    open_counter, close_counter = 1, 0
                    while open_counter != close_counter:
                        if j == len(function):
                            return 'Number of "(" does not equal to the number of ")".'
                        if function[j] == '(':
                            open_counter += 1
                        elif function[j] == ')':
                            close_counter += 1
                        j += 1

                    # Put the found function in the insides
                    new_string.append(function[i:j])

                    # Skip the function
                    i += j - 1

                # Check if lg, ln
                elif function[i:i + 2] in allowed_string_patterns:
                    j = i + 3

                    # Check if hard function with hard insides lg((x + 1) + 2) and for usual lg(x + 1)
                    open_counter, close_counter = 1, 0
                    while open_counter != close_counter:
                        if j == len(function):
                            return 'Number of "(" does not equal to the number of ")".'
                        if function[j] == '(':
                            open_counter += 1
                        elif function[j] == ')':
                            close_counter += 1
                        j += 1

                    # Put the found function in the insides
                    new_string.append(function[i:j])

                    # Skip the function
                    i += j - 1
            if i >= len(function):
                break
            if function[i] == 'x':
                new_string.append(function[i])

            # Check if it`s a number (not only 0-9)
            elif function[i].isnumeric():
                numeric_operator = function[i]
                j = 1
                while i + j < len(function):
                    if function[i + j].isnumeric():
                        numeric_operator += function[i + j]
                    else:
                        break
                    j += 1
                new_string.append(numeric_operator)
                i += j - 1
        i += 1
    # By the end we have a string '1+23^7*123+4' into ['1', '+', '23', '^', '7', '*', '123', '+', '4']

    # Actual handling the calculations


    while len(new_string) > 1:

        # Operators are stored in the order they are calculated in actual math
        for operation_i, operation in enumerate(split_operators):
            i = len(new_string) - 1
            while i > 0:
                if new_string[i] == operation:
                    new_string[i+1] = calculate_two_things([new_string[i - 1], new_string[i + 1]], operation_i)
                    del new_string[i-1:i+1]
                i -= 1

    return str(new_string[0])


# Call for logarifmic or sin
def calculate_function(s):
    new_string = ''
    return new_string


# Calculates two numbers/functions that are by the sides of an operator
def calculate_two_things(nums, operation_index):
    new_string = ''
    num1, num2 = nums[0], nums[1]
    for i in range(0, 2):
        num = str(nums[i])
        if not num.isnumeric():
            # log handle
            if num[0:3] == 'log':
                insides = num[4:-1].split(',')
                if not insides[0].isnumeric():
                    base = calculate(insides[0])
                else:
                    base = insides[0]
                print('asdasdasdasdadasdasd', base, insides)
                if not insides[1].isnumeric():
                    value = calculate(insides[1])
                else:
                    value = insides[1]
                    print('the fuckin log equals to:', str(math.log(float(value), float(base))))
                nums[i] = math.log(float(value), float(base))
            # ln and lg handle
            if num[0:2] == 'lg' or num[0:2] == 'ln':
                insides = num[3:-1]
                if not insides.isnumeric():
                    value = calculate_function(insides)
                else:
                    value = insides
                if num[0:2] == 'lg':
                    nums[i] = math.log(float(value), 10)
                else:
                    nums[i] = math.log(float(value))
            #sin and cos handle
            if num[0:3] == 'sin':
                insides = num[3:-1]
                if not insides.isnumeric():
                    insides = calculate(insides)
                nums[i] = math.sin(float(insides))
            if num[0:3] == 'cos':
                insides = num[3:-1]
                if not insides.isnumeric():
                    insides = calculate(insides)
                nums[i] = math.cos(float(insides))
    num1, num2 = nums[0], nums[1]
    if operation_index == 0:
        return float(num1) ** float(num2)
    if operation_index == 1:
        return float(num1) * float(num2)
    if operation_index == 2:
        return float(num1) / float(num2)
    if operation_index == 3:
        return float(num1) + float(num2)
    if operation_index == 4:
        return float(num1) - float(num2)



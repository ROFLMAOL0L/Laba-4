import input_handler as i_h
from invalid_syntax_handler import check
from try_handler import *
from time import time

def main():
    user_input = check(input('starting\nfunction:\ny='))
    if user_input[0] == 'E':
        print(user_input)
    else:
        x0_input = float_input('beginning of area x= ')
        x1_input = float_input('end of area x= ')
        x_scaling_input1 = float_input('step i (difference between x_i and x_i+1)= ')
        file_name = input('enter file name: ')
        file_format = choice3_input('1) xlsx\n2) turtle\n3) matplotlib\nyour choice: ')
        starting_time = time()
        i_h.handle_input(user_input, file_name, file_format, x0_input, x1_input, x_scaling_input=x_scaling_input1)
        ending_time = time()
        print('program completed in', ending_time - starting_time, 'seconds')

if __name__ == '__main__':
    main()

import input_handler as i_h
from time import time


def main():
    print('Starting')
    print('Введите функцию: ')
    user_input = str(input())
    print('Укажите начало области x: ')
    x0_input = float(input())
    print('Укажите конец области x: ')
    x1_input = float(input())
    print('Укажите шаг i (разница между x_i и x_i+1):')
    x_scaling_input1 = float(input())
    #i_h.handle_input(user_input)
    xls = input('Введите имя xlsx файла - ')
    starting_time = time()
    i_h.handle_input(user_input, xls, x_range_input=(x0_input, x1_input), x_scaling_input=x_scaling_input1)
    ending_time = time()
    print('Программа выполнена за: ', ending_time - starting_time, 'секунд')

if __name__ == '__main__':
    main()

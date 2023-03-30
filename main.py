import input_handler as i_h


def main():
    print('Starting')
    print('Input the function: ')
    user_input = input()
    print(i_h.handle_input(user_input))

if __name__ == '__main__':
    main()

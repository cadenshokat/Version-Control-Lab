def encode_data(number):
    new_num = ''

    for digit in str(number):
        if int(digit) <= 6:
            digit = int(digit) + 3
            new_num += str(digit)
        else:
            digit = int(digit) - 7
            new_num += str(digit)

    return new_num


if __name__ == '__main__':

    password = str(input('Enter your password: '))
    program = True

    while program:

        print("1. Encode Password")
        print("2. Decode Password")
        print("3. Quit")
        print()

        option = int(input('Choose an option: '))

        if option == 1:
            new_password = encode_data(password)
            print(new_password)

        if option == 2:
            print(decode_data(new_password))

        if option == 3:
            program = False

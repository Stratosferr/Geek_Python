with open("5_1.txt", 'w') as user_file:
    while True:
        user_str = input('Введите строку. Если строка пустая ввод будет закончен: ')
        if user_str == '':
            break
        else:
            user_file.write(user_str + '\n')

def my_func():
    """
    выводит на экран сумму чисел из всех введенных пользователем последовательностей
    символьные строки введенные в последовательности не обрабатываются
    ввод последовательностей заканчивается при встрече символа q


    """
    sum_num = 0
    while True:
        user_str = input("введите строку. маркером окончания суммирования является символ 'q': ").split()
        if 'q' in user_str:
            user_str = user_str[:user_str.index('q')]
            for el in user_str:
                try:
                    sum_num += float(el)
                except ValueError:
                    None
            break
        else:
            for el in user_str:
                try:
                    sum_num += float(el)
                except ValueError:
                    None
    print(sum_num)


my_func()

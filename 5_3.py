with open("5_3.txt", "r", encoding='utf-8') as employees:
    cnt = 0
    sum_emp = 0
    for em in employees:
        cnt += 1
        sum_emp += float(em.split()[1])
        if float(em.split()[1]) < 20000:
            print(f'Сотрудник {em.split()[0]} доход менее 20000')
    print(f'Средний доход сотрудников = {sum_emp / cnt}')

with open("5_6.txt", "r", encoding='utf-8') as discipline:
    lect = {}
    for line in discipline:
        subject_info = {line[:line.find(":") + 1]: sum(
            [int(els[:els.find("(")]) for els in line.split() if ('(пр)' in els or '(л)' in els or '(лаб)' in els)]) for
                        el in line}
        lect.update(subject_info)
print(lect)

"""Выполнил проверку не только на пустые данные, в случае отсутствия каких либо типов занятий, но и в случае, если в строке встречены какие либо некорректные данные, они игнорируются"""

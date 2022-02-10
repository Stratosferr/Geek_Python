from itertools import count, cycle

print('итератор генерирующий с помощью функции count целые числа начиная с 5. окончание генерации - число 14')
for x in count(5):
    if x < 14:
        print(x)
    else:
        break

cnt_cycle = 0

print(
    'итератор повторяющий с помощью функции cycle элементы списка cycle_list. повтор элементов заканчивается, когда выведено 13 элементов')
cycle_list = [1, 'A', '%', 6]
for el in cycle(cycle_list):
    if cnt_cycle > 12:
        break
    else:
        print(el)
    cnt_cycle += 1

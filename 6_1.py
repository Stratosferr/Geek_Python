import time
from itertools import cycle


class Traffic():
    __color = {"Red": [7, 31], "Yellow": [2, 33], "Green": [5, 32]}

    def running(self):
        cnt_sec = 0
        print('запущена 30 секундная демонстрация работы светофора')
        for col in cycle(self.__color.keys()):
            cnt_sec += self.__color.get(col)[0]
            print(f"\033[{self.__color.get(col)[1]}m{col}")
            time.sleep(self.__color.get(col)[0])
            if cnt_sec >= 30:
                print('Демонстрация завершена')
                break


a = Traffic().running()

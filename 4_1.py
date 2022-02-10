from sys import argv

scr_name, work_hour, rate, premium = argv
print(f'Заработная плата сотрудника за данный период: {int(work_hour) * int(rate) + int(premium)} тугриков')

with open("5_2.txt", "r") as user_f:
    cnt_str = 0
    for i, line in enumerate(user_f):
        print(f"В {i + 1}-Й строке файла содержится {len(line.split())} слов")
    else:
        print(f"в файле {i + 1} строк")

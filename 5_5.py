from random import randint

out_f = open("5_5_output.txt", "w")
with open("5_5_input.txt", "w+") as in_f:
    for el in range(15):
        in_f.write(str(randint(1, 1000)) + " ")
    in_f.seek(0)
    out_f.write(str(sum(map(int, in_f.read().split()))))
out_f.close()


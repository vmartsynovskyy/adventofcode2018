with open("input.txt") as f:
    file = f.readlines()

sum = 0
sum_list = {0}

found_twice = False

while not found_twice:
    for line in file:
        sum += int(line)
        if sum in sum_list:
            print(sum)
            found_twice = True
            break
        else:
            sum_list |= {sum}

# +3, +3, +4, -2, -4
# 0, 3, 6, 10, 8, 4, 7, 10
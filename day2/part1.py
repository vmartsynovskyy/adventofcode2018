with open("input.txt") as f:
    file = f.readlines()

sum_three_same = 0
sum_two_same = 0

for line in file:
    counted_two = False
    counted_three = False
    for char in line:
        if line.count(char) == 3:
            counted_three = True
        elif line.count(char) == 2:
            counted_two = True
    
    if counted_three:
        sum_three_same += 1
    if counted_two:
        sum_two_same += 1

print(sum_three_same * sum_two_same)
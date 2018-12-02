with open("input.txt") as f:
    file = f.read().splitlines()

min_diff = 1000000000

for line1 in file:
    for line2 in file:
        if line1 == line2:
            continue
        diff_list = []
        for i in range(len(line1)):
            if (line1[i] != line2[i]):
                diff_list.append(line1[i])
        if len(diff_list) < min_diff:
            print("="*10)
            print(diff_list)
            print(len(diff_list))
            print(line1)
            print(line2)
            min_diff = len(diff_list)
addition_str = "2+5+10+20"
numbs = addition_str.split("+")
sum_val = 0
for num in range(len(numbs)):
    sum_val += int(numbs[num])
print(sum_val)
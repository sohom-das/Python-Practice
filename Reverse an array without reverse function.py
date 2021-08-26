print("Enter an array of numbers: ", end = " ")
num = list(map(int, input().split(",")))
num_rev = []
n = len(num)

print("Array length of numbers: ", n)

i = n

i = i-1

for k in range(n):
    num_rev.append(num[i])
    i -= 1

print("Reversed array: ", num_rev)
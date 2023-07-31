from sys import stdin
num1, num2 = stdin.readline().split()
num1 = int(num1[::-1])
num2 = int(num2[::-1])
print(num1 if num1 > num2 else num2)

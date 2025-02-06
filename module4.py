#!/usr/bin/python3

flag = True
N = 0
while flag:
    N = int(input('Enter a positive integer: '))
    if N % 2 == 0:
        flag = False

numbers = []
for i in range(N):
    n = int(input(f"Enter number {i+1}: "))
    numbers.append(n)

X = int(input('Enter X integer: '))

if X in numbers:
    print(numbers.index(X)+1)
else:
    print('-1')


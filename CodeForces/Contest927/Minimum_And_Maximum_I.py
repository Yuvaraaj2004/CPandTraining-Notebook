from math import ceil


for i in range(int(input())):
    n = int(input())
    if n % 2:
        print(n//2*(n//2+1)+ceil(n/2))
    else:
        print(n//2*(n//2+1))

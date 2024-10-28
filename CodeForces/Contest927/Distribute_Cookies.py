from math import ceil
# cook your dish here
t = int(input())
while t:
    a, b = map(int, input().split())
    if a > b:
        print(a-b)
    elif b-b//a*a < ceil(b/a)*a-b:
        print(b-b//a*a)
    else:
        print(ceil(b/a)*a-b)
    t -= 1

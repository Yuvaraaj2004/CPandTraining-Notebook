from math import log2


def factorial(x):


i = 1
mz = 0
try:
    c = 0
    while len(str(i)) < 4300:
        print(c, len(str(i)))
        mx = i
        i *= 2
        c += 1
except Exception as e:
    print(e)
print('log', log2(i))
# print(i)

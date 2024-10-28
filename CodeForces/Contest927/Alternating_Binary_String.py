
def f(s=0):
    fg = 0
    for ind, i in enumerate(l):
        if (not ind & 1 and s != (int(i)+fg) & 1) or (ind & 1 and s == (int(i)+fg) & 1):
            fg += 1
    return fg


for t in range(int(input())):
    n = int(input())
    l = input()

    print(min(f(0), f(1)))


# cook your dish here

t = int(input())

l = [[] for i in range(3)]

for i in range(26):

    l[i % 3].append(i)

d = {}

for ind, i in enumerate(l[0]+l[1]+l[2]):

    d[chr(ord('A')+i)] = ind+1

print(d)

while t:

    n = int(input())

    a, b = input(), input()

    print(*[d[b[i]]-d[a[i]] if d[b[i]]-d[a[i]] >=
          0 else 26-(-d[b[i]]+d[a[i]]) for i in range(n)])

    t -= 1

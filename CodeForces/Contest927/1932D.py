t=int(input())
for test in range(t):
    rows,trump=int(input()),input()
    d={i:[] for i in 'SCDH'}
    c = {i: 0 for i in 'SCDH'}
    for i in input().split():
        d[i[1]].append(int(i[0]))
        c[i[1]]+=1
    diff=(c[trump]-sum(c[i]%2 for i in 'SCDH' if i!=trump))
    if diff<0 or diff%2!=0:
        print('IMPOSSIBLE')
        continue
    # print(trump,d,diff)

    for i in d:
        d[i].sort()
        if i !=trump:
            while d[i] and len(d[i])!=1:
                print(f'{d[i].pop(0)}{i} {d[i].pop(0)}{i}')
            if d[i]:
                print(f'{d[i].pop(0)}{i} {d[trump].pop(0)}{trump}')
    while d[trump] and len(d[trump]) != 1:
        print(f'{d[trump].pop(0)}{trump} {d[trump].pop(0)}{trump}')

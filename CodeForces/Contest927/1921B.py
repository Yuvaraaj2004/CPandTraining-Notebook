t=int(input())
for t in range(t):
    n=int(input())
    a,b=input(),input()
    print(sum(1 if b[i] == '1' and a[i] == '0' else 0 for i in range(n)))



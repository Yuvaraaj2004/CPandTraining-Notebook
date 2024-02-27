t = int(input())
for t in range(1, t+1):
    print(f"Case #{t}:")
    a,b=map(int,input().split())
    for i in range(2*a+1):
        s=''
        if i==0 or i==1:
            s+='..'
        s+=('+-' if i%2==0 else '|.')*(b-len(s)//2)+('+' if i%2==0 else '|')
        print(s)
        # print()


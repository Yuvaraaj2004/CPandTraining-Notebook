n=int(input())
for i in range(n):
    l=int(input())
    s=input()
    i,j=0,l-1
    while i<l and s[i]=='W':i+=1
    while j>=0 and s[j]=='W':j-=1
    print(j-i+1)
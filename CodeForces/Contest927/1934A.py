for i in range(int(input())):
    n = int(input())
    l = sorted(map(int, input().split()))
    (ai, aj), (ak, al) = l[0:2], l[-2:]
    print(abs(ai-al)+abs(al-aj)+abs(aj-ak)+abs(ak-ai))

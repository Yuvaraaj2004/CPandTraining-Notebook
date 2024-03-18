for i in range(int(input())):
    attend, mark = list(map(int, input().split()))
    if attend < 50:
        print("Z")
    else:
        if mark < 50:
            print("F")
        else:
            print("A")

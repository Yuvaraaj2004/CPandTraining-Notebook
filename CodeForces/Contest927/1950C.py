for t in range(int(input())):
    a, b = list(map(str, input().split(":")))
    if int(a) >= 12 or 0 == int(a):
        a = int(a)-12
        if a < 0:
            a += 12
        print(f"{'0' if a < 10 else ''}{a}:{b} PM")
    else:
        print(f"{a}:{b} AM")

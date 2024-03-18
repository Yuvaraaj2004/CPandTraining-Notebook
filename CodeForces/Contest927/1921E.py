for t in range(int(input())):
    h, w, ax, ay, bx, by = map(int, input().split())
    print(f"{t}", 'Draw' if bx-ax <= 0 or (abs(by-ay) > abs(ax-bx))
          else ('Alice' if (ax-bx) % 2 else 'Bob'))

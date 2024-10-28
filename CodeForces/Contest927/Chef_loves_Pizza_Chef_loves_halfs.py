
import math


for t in range(int(input())):
    n = int(input())
    close = n % (1 << math.floor(math.log2(n)))
    # print(0 if close == 0 else 1 << (close+1))
    print(close*2)

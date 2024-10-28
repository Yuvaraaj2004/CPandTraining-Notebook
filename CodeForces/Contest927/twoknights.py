d = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]


def f(num):
    n, ans, exist = num*num, 0, lambda x, y: x >= 0 and y >= 0 and x < num and y < num
    d = {1:0,
         2:12,
         3:56,
         4:192,}
    if i in d:return d[i]
    def g(i, j):
        count = 1
        for x, y in d:
            xc, yc = i+x, j+y
            if exist(xc, yc):
                count += 1
        return n-count
    s={}

    return 


n = int(input)
for i in range(1, n+1):
    print(f(i))

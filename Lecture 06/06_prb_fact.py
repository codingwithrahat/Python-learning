def f(n):
    f = 1
    

    for i in range(1, n + 1):
        f *= i

    return f


res = f(5)

print(res)
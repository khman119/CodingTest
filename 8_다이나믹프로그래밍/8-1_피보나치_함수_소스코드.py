def fibo(x):
    if x == 1 or x == 2:
        return 1
    else:
        return fibo(x-2) + fibo(x-1)

print(fibo(5))
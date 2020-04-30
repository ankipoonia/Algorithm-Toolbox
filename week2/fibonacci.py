# Uses python3
def calc_fib(n):
    if n<=1:
        return n
    else:
        a = 0
        b = 1
        for i in range(1,n):
            temp = b
            b = a+b
            a = temp
        return b
n = int(input())
print(calc_fib(n))

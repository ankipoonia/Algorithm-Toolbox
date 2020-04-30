# Uses python3
def lcm_naive(a, b):
    if a>b:
        for l in range(a, a*b + 1,a):
            if l % a == 0 and l % b == 0:
                return l
    else:
        for l in range(b, a*b + 1,b):
            if l % a == 0 and l % b == 0:
                return l

    return a*b

if __name__ == '__main__':
    a, b = input().split()
    a = int(a)
    b = int(b)
    print(lcm_naive(a, b))

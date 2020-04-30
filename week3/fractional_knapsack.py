# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    vperw = []
    for i in range(0,len(weights)):
        vperw.append([i,values[i]/weights[i]])

    vperw.sort(key = lambda x: x[1])
    j = len(vperw)
    while capacity>0:
        j = j - 1
        if weights[vperw[j][0]]<=capacity:
            value = value + capacity*vperw[j][1]
            capacity = 0
        else:
            value = value + values[vperw[j][0]]
            capacity = capacity - weights[vperw[j][0]]

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

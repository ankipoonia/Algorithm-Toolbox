# Uses python3
import sys

def get_change(m):
    #write your code here
    x = m//10
    y1 = m - x*10
    y = y1//5
    z = y1 - y*5
    m = x + y + z
    return m

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))

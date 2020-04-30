# python3


def max_pairwise_product(numbers):
    l = sorted(numbers,reverse=True)
    max_product = l[0]*l[1]
    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))

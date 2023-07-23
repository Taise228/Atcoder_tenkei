def gcd(a, b):
    """find the greatest common divisor of a and b
    
    Args:
        a (int): a number
        b (int): another number

    Returns:
        int: the greatest common divisor of a and b
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    

def gcd_list(numbers):
    """find the greatest common divisor of a list of numbers
    
    Args:
        numbers (list): a list of numbers

    Returns:
        int: the greatest common divisor of the numbers in the list
    """
    if len(numbers) == 1:
        return numbers[0]
    else:
        return gcd(numbers[0], gcd_list(numbers[1:]))


def main():
    A, B, C = map(int, input().split())

    gcd = gcd_list([A, B, C])

    count = (A // gcd - 1) + (B // gcd - 1) + (C // gcd - 1)
    print(count)
    

if __name__ == '__main__':
    main()

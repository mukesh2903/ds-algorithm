def reverse_number(num):
    reversed_number = 0
    while num > 0:
        remainder = num % 10
        reversed_number = reversed_number * 10 + remainder
        num = num // 10
    return reversed_number


if __name__ == "__main__":
    print(reverse_number(1234))
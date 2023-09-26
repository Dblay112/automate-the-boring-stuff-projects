# Bright Djogatse
# collatz sequence
#!/usr/bin/python3


def collatz(number):
    """collatz function"""
    if number % 2 == 0:
        print("number // 2")
        return number
    else:
        number % 2 == 1
        print("3 * number + 1")
        return 3 * number + 1

if __name__ == "__main__":

    try:
        user = int(input("Enter number:"))
        result = collatz(user)
        while (result != 1):
            result = collatz(result)
    except ValueError:
        print("number must be an integer")

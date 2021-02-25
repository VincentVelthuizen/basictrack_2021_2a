def get_five_numbers():
    total = 0
    for i in range(5):
        number = int(input("Give a number "))
        total = total + number
    return total


def get_numbers(how_many):
    total = 0
    for i in range(how_many):
        number = int(input("Give a number "))
        total = total + number
    return total


def get_user_input():
    total = 0

    number = int(input("Give a number (0 to stop) "))
    while number != 0:
        total += number

        number = int(input("Give a number (0 to stop) "))

    return total


if __name__ == '__main__':
    # this is where I'll write all my code

    total_of_five_numbers = get_user_input()
    print(total_of_five_numbers)

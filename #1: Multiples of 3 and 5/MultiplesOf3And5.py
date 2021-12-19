# Problem 1: Multiples of 3 and 5
# Find the sum of all the multiples of 3 or 5 below 1000.

def main():
    sum_of_multiples(1000)

    # Uncomment the below lines to allow user input of the function

    # user_range = int(input("Name the number you want the sum of multiples from: "))
    # sum_of_multiples(user_range)


def sum_of_multiples(user_range):
    euler_sum = 0
    for i in range(user_range):
        if i % 3 == 0 or i % 5 == 0:
            euler_sum += i
    print(f"Sum of multiples of 3 and 5 below {user_range}: {euler_sum}")


if __name__ == '__main__':
    main()

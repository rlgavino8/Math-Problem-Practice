# Problem 2: Even Fibonacci Numbers
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find
# the sum of the even-valued terms.

def main():
    current_fib = 0
    first_fib = 0
    second_fib = 1
    even_fibs_sum = 0
    while current_fib < 4000000:
        current_fib = first_fib + second_fib
        if current_fib % 2 == 0:
            even_fibs_sum += current_fib
        first_fib = second_fib
        second_fib = current_fib
    print(even_fibs_sum)


if __name__ == '__main__':
    main()

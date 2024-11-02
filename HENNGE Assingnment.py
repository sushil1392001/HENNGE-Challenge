def sum_of_square(x_input, sum, x_time_square_input, l):
    try:
        if x_time_square_input <= 0:
            return sum
        x = x_input[l]
        x = int(x)
        if x > 0:
            sum += x * x
        l += 1
        x_time_square_input -= 1
        return sum_of_square(x_input, sum, x_time_square_input, l)
    except:
        return 'Please check your input format'


def N_time_input(N, result=''):
    try:
        if N <= 0:
            return result
        x_time_square_input = int(input(''))
        x_input = input('').split()
        total = sum_of_square(x_input, 0, x_time_square_input, 0)
        N -= 1
        return N_time_input(N, result + str(total) + "\n")
    except:
        return 'Please check your input format'


def main():
    # N always greater than 0
    try:
        N = int(input(""))
        print(N_time_input(N))
    except:
        print('Please check your input format')


if __name__ == "__main__":
    main()

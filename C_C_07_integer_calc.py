# Calculates number of bits needed to represent text in ascii
def int_check(question, low):
    error = "Please enter a number that is more than zero\n"
    while True:

        try:
            # ask the user for a number
            response = int(input(question))

            # check that the number is more than zero
            if response >= low:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine goes here
def integer_calc():
    integer = int_check("Integer: ", 0)

    raw_binary = bin(integer)

    binary = raw_binary[2:]
    num_bits = len(binary)

    answer = "{} in binary is {}. We ned {} tp represent it."

    return answer


integer_ans = integer_calc()
print(integer_ans)

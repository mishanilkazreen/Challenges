# If we list all the antural numbers below that are multiples of 3 or 5, we get 3, 5, 6, and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def CheckMultiple(number, multiples_list):

    for i in multiples_list:
        if number % i == 0:
            return True

    return False

def CalculateSumOfList(list):
    total = 0

    for i in list:
        total = total + i

    return total

isRunning = True
while isRunning:
    multiples_list = [3, 5]
    numbers_in_multiples = []
    max_number = 1000

    for i in range(max_number):
        retval = CheckMultiple(i, multiples_list)

        if retval:
            numbers_in_multiples.append(i)

    sum_total = CalculateSumOfList(numbers_in_multiples)

    print(f"The sum of all the multiples of {multiples_list} below {max_number} is {sum_total}")

    isRunning = False
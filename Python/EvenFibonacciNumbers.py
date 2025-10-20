def check_even(number):

    if number % 2 == 0:
        return True

    return False

def filter_even(list):

    return [n for n in list if check_even(n)]

def fibonacci_sequenece(list, base_case):

    next_number = list[::-1][0] + list[::-1][1]

    if next_number < base_case: ## Checks to see if the last number exceeds the base_case
        list.append(next_number)
    else:
        return list

    return fibonacci_sequenece(list, base_case)

if __name__ == "__main__":
    sequence = fibonacci_sequenece([1,2], 4000000)
    even_numbers = filter_even(sequence)
    total = sum(even_numbers)

    print(total)

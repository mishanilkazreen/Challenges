def CheckEven(number):

    if number % 2 == 0:
        return True

    return False

def FilterEven(list):

    return [n for n in list if CheckEven(n)]

def CalculateSumOfList(list):
    total = 0

    for i in list:
        total = total + i

    return total

def FibonacciSequence(list, base_case):

    next_number = list[::-1][0] + list[::-1][1]

    if next_number < base_case: ## Checks to see if the last number exceeds the base_case
        list.append(next_number)
    else:
        return list

    return FibonacciSequence(list, base_case)

if __name__ == "__main__":
    Sequence = FibonacciSequence([1,2], 4000000)
    EvenNumbers = FilterEven(Sequence)
    Total = CalculateSumOfList(EvenNumbers)

    print(Total)

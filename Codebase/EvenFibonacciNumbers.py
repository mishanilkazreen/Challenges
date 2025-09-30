from os import device_encoding


def CheckEven(number):

    if number % 2 == 0:
        return True

    return False

def SeperateListsByProperties(setting, list): # 0 = Even only, 1 = Odd Only
    if setting == 0:
        for i in list:
            retval = CheckEven(i)
            print(retval, i)
            if not retval:
                list.remove(i)

    return list


def FibonacciSequence(list, base_case):

    last_number = list[::-1][0] + list[::-1][1]

    if last_number < base_case: ## Checks to see if the last number exceeds the base_case
        list.append(last_number)
    else:
        return list

    return FibonacciSequence(list, base_case)

Sequence = FibonacciSequence([1,2], 4000000)
EvenNumbers = SeperateListsByProperties(0, Sequence)

print(EvenNumbers)

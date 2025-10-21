def check_palindrome(text):
    text = str(text)

    # Check if the original and reverse strings are equal
    if text == text[::-1]:
        return True

    return False


def largest_palindrome_product():
    max_palindrome = 0

    # Starting from the top to the bottom, as when we find the first palindrome
    # then we know it is the biggest.
    for num_1 in range(999, 99, -1):

        for num_2 in range(999, 99, -1):
            product = num_1 * num_2

            if check_palindrome(product) and product > max_palindrome:
                max_palindrome = product
                factors = (num_1, num_2)


    print(f"{factors[0]} x {factors[1]} = {max_palindrome}")

    return None

largest_palindrome_product()
# Mathematical Logic Used:
# p_n = p1 * p2 * p3 ... * p_n-1

def calculate_largest_prime_factor(number: int) -> int:
    largest_prime_factor = None

    # Base Case
    if number <= 1:
        return None

    if number // 2 == 0:
        number = number / 2
        largest_prime_factor = 2

    # i = 2n + 1
    i = 3
    while i*i <= number:

        # See if i is a factor
        while number % i == 0:
            largest_prime_factor = i
            number //= i

        i += 2

    if number > 1:
        largest_prime_factor = number

    return largest_prime_factor



if __name__ == "__main__":
    largest_prime_factor = calculate_largest_prime_factor(600851475143)

    print(largest_prime_factor)
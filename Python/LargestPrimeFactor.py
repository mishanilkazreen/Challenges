def calculate_larget_prime_factor(number: int) -> int:
    largest_prime_factor = None

    # Base Case
    if number <= 1:
        return None

    if number // 2 == 0:
        number = number / 2
        largest_prime_factor = 2






retval = calculate_larget_prime_factor(600851475143)
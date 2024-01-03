import random

def generate_random_numbers(lower_limit, upper_limit, count):
    return [random.randint(lower_limit, upper_limit) for _ in range(count)]


random_numbers = generate_random_numbers(1, 100, 5)
print(random_numbers)

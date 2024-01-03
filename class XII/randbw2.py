import random

def random_number_between(lower_limit, upper_limit):
    return random.randint(lower_limit, upper_limit)

result = random_number_between(10, 50)
print(result)

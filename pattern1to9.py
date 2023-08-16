import random

def generate_random_pattern():
    digits = list(range(1, 10))
    random.shuffle(digits)
    pattern = ''.join(map(str, digits))
    return pattern

random_pattern = generate_random_pattern()
print(random_pattern)

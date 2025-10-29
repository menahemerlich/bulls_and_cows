import random


def generate_secret(length: int = 4, *, unique_digits: bool = True, allow_leading_zero: bool = False, rng: random.Random | None = None) -> str:
    secret = ""
    num_list = []
    while len(num_list) < 4:
        num = random.randint(1, 9)
        if num not in num_list:
            num_list.append(num)
    for i in num_list:
        secret += str(i)
    return secret




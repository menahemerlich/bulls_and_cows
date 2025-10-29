import random


def generate_secret(length: int = 4) -> str:
    secret = ""
    num_list = []
    while len(num_list) < length:
        num = random.randint(1, 9)
        if num not in num_list:
            num_list.append(num)
    for i in num_list:
        secret += str(i)
    return secret

def is_valid_guess(guess: str, length: int) -> tuple[bool, str]:
    if len(guess) == length and guess.isdigit():
        return True, guess
    return False, guess

def is_new_guess(guess: str, history:list[str]) -> bool:
    if guess in history:
        print("אתה חוזר על עצמך...")
        return False
    return True



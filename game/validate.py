
def is_valid_guess(guess: str, length: int) -> tuple[bool, str]:
    if len(guess) == length and guess.isdigit():
        return True, guess
    print("Typo error!!")
    return False, guess

def is_new_guess(guess: str, history:list[str]) -> bool:
    if guess in history:
        print("אתה חוזר על עצמך...")
        return False
    return True
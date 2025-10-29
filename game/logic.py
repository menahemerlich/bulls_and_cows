
def score_guess(secret: str, guess: str) -> tuple[int, int]:
    bulls = 0
    cows = 0
    for i in range(len(guess)):
        if secret[i] == guess[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows

def is_won(state: dict, length: int) -> bool:
    if state["bulls"] == length:
        return True
    return False

def game_state(secret: str, length:int) -> dict:
    state = {
        "secret": secret,
        "length": length,
        "history": [],
        "seen": [],
        "bulls": 0
    }
    return state

def apply_guess(state: dict, guess: str, bulls_cows: tuple[int, int]) -> tuple[int, int]:
    state["history"].append(guess)
    state["bulls"] = bulls_cows[0]
    state["seen"].append((guess, bulls_cows[0], bulls_cows[1]))
    return bulls_cows[0], bulls_cows[1]












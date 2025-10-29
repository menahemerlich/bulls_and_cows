
def score_guess(secret: str, guess: str) -> tuple[int, int]:
    bulls = 0
    cows = 0
    for i in range(len(guess)):
        if secret[i] == guess[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows

def is_won(bulls: int, length: int) -> bool:
    if bulls == length:
        return True
    return False

def game_state(secret: str, length:int, guess: str, bulls_cows: tuple[int, int] ) -> dict:
    game_info = {
        "secret": secret,
        "length": length,
        "history": [],
        "seen": [f"guess: {guess}, bulls: {bulls_cows[0]}, cows: {bulls_cows[1]}"]
    }
    return game_info









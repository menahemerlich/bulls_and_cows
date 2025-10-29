
def score_guess(secret: str, guess: str) -> tuple[int, int]:
    bulls = 0
    cows = 0
    for i in range(len(guess)):
        if secret[i] == guess[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows


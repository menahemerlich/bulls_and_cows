
def prompt_guess() -> str:
    guess = input("Enter your guess: ")
    return guess

def print_feedback(guess: str, bulls: int, cows: int) -> None:
    print(f"your guess: {guess}\n"
          f"your bulls: {bulls}\n"
          f"your cows: {cows}")






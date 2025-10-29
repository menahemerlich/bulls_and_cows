
def prompt_guess() -> str:
    guess = input("Enter your guess: ")
    return guess

def print_feedback(guess: str, bulls: int, cows: int) -> None:
    print(f"your guess: {guess}\n"
          f"your bulls: {bulls}\n"
          f"your cows: {cows}")

def print_status(state: dict) -> None:
    print(f"your history: ")
    for i in state["seen"]:
        print(f"              your guess: {i[0]}, your bulls: {i[1]}, your cows: {i[2]}")
    print(f"step_count: {state["step_count"]}")

def print_result(state: dict):
    print(f"you win in {state["step_count"]} steps!!!! the number is {state["secret"]}")





from game.secret import generate_secret
from game.validate import is_valid_guess, is_new_guess
from game.logic import score_guess, is_won, game_state, apply_guess
from game.io import prompt_guess, print_feedback, print_status, print_result

length = 4
def play(length: int):
    secret = generate_secret()
    game_info = game_state(secret, 4)
    while not is_won(game_info, length):
        guess = prompt_guess()
        if is_valid_guess(guess, length) and is_new_guess(guess, game_info["history"]):
            bulls_and_cows = score_guess(secret, guess)
            apply_guess(game_info, guess, bulls_and_cows)
            print_feedback(guess, bulls_and_cows[0], bulls_and_cows[1])

            print_status(game_info)
    print_result(game_info)

play(4)



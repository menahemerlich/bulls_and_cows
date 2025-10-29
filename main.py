from game.secret import generate_secret
from game.validate import is_valid_guess, is_new_guess
from game.logic import score_guess, is_won, game_state, apply_guess
from game.io import prompt_guess, print_feedback

guess = prompt_guess()
secret = generate_secret()
game_info = game_state(secret, 4)
# print(is_valid_guess("02002", 4))
# print(is_new_guess("22", ["000", "224"]))
bulls_and_cows = (score_guess(secret, guess))
print(is_won(bulls_and_cows[0], 4))
print(game_info)
print(apply_guess(game_info, guess, bulls_and_cows))
print(game_info)
print_feedback(guess, bulls_and_cows[0], bulls_and_cows[1])






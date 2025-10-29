from game.secret import generate_secret, is_valid_guess, is_new_guess
from game.logic import score_guess, is_won, game_state, apply_guess

guess = "1234"
secret = generate_secret()
game_info = game_state(secret, 4)
# print(is_valid_guess("02002", 4))
# print(is_new_guess("22", ["000", "224"]))
bulls = (score_guess(secret, guess))
print(is_won(bulls[0], 4))
print(game_info)
print(apply_guess(game_info, guess, bulls))
print(game_info)






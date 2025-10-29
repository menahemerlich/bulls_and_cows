from game.secret import generate_secret, is_valid_guess, is_new_guess
from game.logic import score_guess, is_won, game_state


secret = generate_secret()
print(is_valid_guess("02002", 4))
print(is_new_guess("22", ["000", "224"]))
bulls = (score_guess(secret, "1234"))
print(is_won(bulls[0], 4))
print(game_state(secret, 4, "1234", bulls ))





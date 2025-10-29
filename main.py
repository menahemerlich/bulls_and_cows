from game.secret import generate_secret, is_valid_guess, is_new_guess
from game.logic import score_guess, is_won


print(generate_secret())
print(is_valid_guess("02002", 4))
print(is_new_guess("22", ["000", "224"]))
bulls = (score_guess("1234", "5234"))
print(is_won(bulls[0], 4))





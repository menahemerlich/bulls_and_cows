from game.secret import generate_secret, is_valid_guess, is_new_guess


print(generate_secret())
print(is_valid_guess("22"))
print(is_new_guess("2", ["5", "0", "2"]))




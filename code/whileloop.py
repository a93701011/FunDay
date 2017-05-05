def get_guess(good_guesses,bad_guesses):
		while True: #always return a letter
				guess = input('Guess a letter: ').lower()
				if len(guess)!=1:
						print("you can only input a single letter")
				elif guess in good_guesses or guess in bad_guesses:
						print("you've already guessed that letter")
				elif not guess.isalpha():
						print("you can only guess a letter")
				else:
						return guess


guess=get_guess([],[])
print(guess)
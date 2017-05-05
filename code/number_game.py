import random
def game():
		# generate a random number between 1 to 10
		secret_number = random.randint(1,10)
		# limit the number of guesses
		guesses = []
		while len(guesses) < 5:
				# get a guess number from the player
				# catch someone submit a non-integer
				try:
						guess = int(input("Guess a number between 1 to 10!"))
				except ValueError:
						print("{} is not integer!".format(guess))
				else:
						# compare guess to secret number
						if guess == secret_number:
							print("You got it! My number is {}".format(secret_number))
							break	
						# Print "too low" or "too high" messages for bad guess
						elif guess > secret_number:
							print("guess lower")
						elif guess < secret_number:
							print("guess higher")
						# print hit/miss
						else :
							print("That's not it!")
				guesses.append(guess)
		else:
				print("You didn't get it,My number is {}".format(secret_number))
		play_again = input("Do you want play again? Y/n")
		if play_again!="n":
				game()
		else:
				print("Bye!")
game()
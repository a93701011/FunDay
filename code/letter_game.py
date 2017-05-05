import os
import random
import sys
#make a list of words
words = [
		'apple',
		'orange',
		'ccoount',
		'strawberry'
		'lime',
		'lemon',
		'melon',
		'grapefruit',
		'kumquart',
	  'blueberry'
]

# Clear screen 
def clear():
		if os.name =='nt':
				os.system('cls')
		else:
				os.system('clear')
# draw letter, guesses, secret word
def draw(bad_guesses,good_guesses,secret_word):
		
		print('Strikes: {}/7'.format(len(bad_guesses)))
		print('')
		
		for letter in bad_guesses:
				print(letter, end=' ')
		print('\n\n')
		
		for letter in secret_word:
				if letter in good_guesses:
						print(letter, end='')
				else:
						print('_',end='')
		print('')		
# take a guess letter
def get_guess(bad_guesses,good_guesses):
	
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

def play(done):
		secret_word = random.choice(words)
		good_guesses = []
		bad_guesses = []
		
		while True :
				clear()
				draw(bad_guesses,good_guesses,secret_word)
				guess = get_guess(bad_guesses,good_guesses)
				
				if guess in secret_word:
						good_guesses.append(guess)
						found = True
						for letter in secret_word:
								if letter not in good_guesses:
										found=False
						if found:
								print("You Win")
								print("My secret word is {}".format(secret_word))
								done = True
				else:
						bad_guesses.append(guess)
						if bad_guesses == 7:
								print("you lost")
								print("My secret word is {}".format(secret_word))
								done = True
				if done:
						play_again = input("play again Y/n ? ").lower()
						if play_again != 'n':
								return play(done=False)
						else:
								sys.exit()

def welcome():
		start = input("Press enter/return to start or Q to quit the game").lower()
		if start =='q':
				print("Bye!")
				sys.exit()
		else:
				return True
# Start 	
print("welcome to letter game")

done=False

while True :
		clear()
		welcome()
		play(done)

				
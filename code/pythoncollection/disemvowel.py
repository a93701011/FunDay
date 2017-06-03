def disemvowel(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    keep_list = []
    for letter in word:
        if letter.lower() not in vowels:
            keep_list.append(letter)
				else:
						pass
    return ''.join(keep_list)
	
my_word=input("What word you would like to disemvowel?\n> ")
print(disemvowel(my_word))
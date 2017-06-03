def word_count(string):
    word_list = string.lower().split()
    new_word_dict = {}
    for word in word_list:
        new_word_dict[word]=word_list.count(word)
    return new_word_dict
	
statistic = word_count("I An a boy")
print(statistic)
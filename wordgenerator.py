import random
words = open('words', 'r')

word_list = []
for word in words:
	word_list.append(word.strip())

misspell_options = ['case', 'repeat']
while(True):
	# Choose a random english word to start with
	start_word = random.choice(word_list)
	list_word = list(start_word)
	vowels = 'aeiou'

	for i in range(0, len(list_word)):
		# Change each vowel with 30% probability
		if list_word[i] in vowels:
			if random.randint(1, 10) <= 3:
				list_word[i] = random.choice(vowels)

		random_from_ten = random.randint(1, 10)
		# Make one mistake with 20% probability (may or may not occur after changing vowel)
		if random_from_ten <= 2:
			option = random.choice(misspell_options)
			if option == 'case':
				list_word[i] = list_word[i].upper()
			elif option == 'repeat':
				list_word[i] *= 2
		elif random_from_ten <= 3:
			list_word[i] = list_word[i].upper()
			list_word[i] *= 2
	print ''.join(list_word)

		

		
		


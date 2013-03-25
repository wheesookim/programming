def count(string):

	count = 0

	for char in string:
		if char == 'e':
			count += 1
		else:
			count += 0 

	print count

count("next people")
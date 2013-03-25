def value():
	x = input("input the number : ")

	if x > 0 and x < 10:
		print x + 10
	elif x > 10 and x < 100:
		print 0.1 * x
	else:
		print 'False'

value()
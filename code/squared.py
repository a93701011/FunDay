def squared(argument):
	try:
		return int(argument)**2
	except ValueError:
		return argument*len(argument)
squared(4)
squared("4")
squared("four")


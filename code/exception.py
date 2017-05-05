while True:	
	try:
			count=int(input("Please input a number!"))
	except ValueError:
		  print("This is not a number!")
	else:
   	  print(count) 
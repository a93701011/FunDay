import random


def even_odd(num):
    # If % 2 is 0, the number is even.
    # Since 0 is falsey, we have to invert it with not.
    if not num % 2: 
        return not num % 2
start = 5 
while start:
    num_rand=random.randint(1, 99)
    if even_odd(num_rand):
        print("{} is even".format(num_rand))
    else:
        print("{} is odd".format(num_rand))
		start -= 1
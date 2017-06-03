#packing dictionary
def packer(**kwargs):
		print(kwargs)
		print("{first_name} {last_name}".format(**kwargs))

#unpacking dictionary
def unpacker(first_name,last_name,job):
		if first_name and last_name:
				print("{} {}".format(first_name,last_name))
		else:
				print(job)
				
packer(first_name="karen",last_name="ku")
unpacker(**{"first_name":"Karen","last_name":"Ku","job":"Engineer"})
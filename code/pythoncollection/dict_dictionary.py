dict ={"first_name":"Karen","last_name":"Ku","Job":"Engineer"}
#dictionary is mutable, unsorted

#Add items
#--------------------------------------
dict["old"]="30up"
dict.update({"old":"30up","job":"X"})

#Delete item
#--------------------------------------
del dict("job")

#Pop item
#--------------------------------------
dict.pop("job") #return value
dict.popitem()	#return random key/value

#Clear dictionary
#--------------------------------------
dict.clear()

#String 
#--------------------------------------
print("my name is {first_name}".format(**dict))


#for loop of dictionary
#--------------------------------------
for key in dict.keys():
		print(key)
for value in dict.values():
		print(value)
for item in dict.items():
		print(item)
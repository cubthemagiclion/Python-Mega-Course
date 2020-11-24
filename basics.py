with open("hey.txt", "a+") as file:
	file.seek(0)
	cont = file.read()
	file.seek(0)
	file.write(cont)
#have to ask teacher for this one.

# write a program that interacts below:
# Say something: Hello
# Say Something: how are you
# Hello. How are you?
'''
def sentences_modification(stringa):
	caped = stringa.capitalize()
	questions = ("How","What","Why")
	if(caped.startswith(questions)):
		caped = caped + "?"
	else:
		caped += "."
	
	return caped

l = []
while True:
	user_input = input("Say something:")
	if user_input == "/end":
		break
	else:
		l.append(sentences_modification(user_input)) 

print(" ".join(l))
'''

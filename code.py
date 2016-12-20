#create a codeword replace abcdefghijklmnopqrstuvwxyz to qwertyuiopasdfghjklzxcvbnm;

saying = input("please enter your phrase, it will now do complex math to encode it: ")
#get the string and put it into an array. too lazy to learn pointers
saying = list(saying) #use the class list to store a list of common characaters into an array (I think)
#print (saying) # you need paranthesis for saying i think now. now lets convert 
i = 0
while i < len(saying): # len class grabs the length of array saying
	if saying[i] == 'a': 
		saying[i] = 'q' 
	elif saying [i] == 'b':
		saying[i] = 'w'
	elif saying [i] == 'c':
		saying[i] = 'e'	
	elif saying [i] == 'd':
		saying[i] = 'r'
	elif saying [i] == 'e':
		saying[i] = 't'
	elif saying [i] == 'f':
		saying[i] = 'y'
	elif saying [i] == 'g':
		saying[i] = 'u'
	elif saying [i] == 'h':
		saying[i] = 'i'
	elif saying [i] == 'i':
		saying[i] = 'o'
	elif saying [i] == 'j':
		saying[i] = 'p'
	elif saying [i] == 'k':
		saying[i] = 'a'
	elif saying [i] == 'l':
		saying[i] = 's'	
	elif saying [i] == 'm':
		saying[i] = 'd'
	elif saying [i] == 'n':
		saying[i] = 'f'
	elif saying [i] == 'o':
		saying[i] = 'g'
	elif saying [i] == 'p':
		saying[i] = 'h'
	elif saying [i] == 'q':
		saying[i] = 'j'
	elif saying [i] == 'r':
		saying[i] = 'k'
	elif saying [i] == 's':
		saying[i] = 'l'
	elif saying [i] == 't':
		saying[i] = 'z'
	elif saying [i] == 'u':
		saying[i] = 'x'
	elif saying [i] == 'v':
		saying[i] = 'c'
	elif saying [i] == 'w':
		saying[i] = 'v'
	elif saying [i] == 'x':
		saying[i] = 'b'
	elif saying [i] == 'y':
		saying[i] = 'n'
	elif saying [i] == 'z':
		saying[i] = 'm'
	
	i = i+1

saying = "".join(saying) # use join method to concatanate the list into a string 
print (saying) 

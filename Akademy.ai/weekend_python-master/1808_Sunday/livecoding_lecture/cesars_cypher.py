def main():
	cypher(20, "./message.txt")


def cypher(key, file):
	f= open(file,"r")
	w = open("chyper.txt", "w+")
	f1 =f.readlines()
	for line in f1:
		char_list = []
		if line =='\n':
			print("found an empty line")
		else:
			for char in line.lower():
				if char.isalpha():	
					if (ord(char) + key) >= 122:
						new_char = chr(97 + ord(char) + key - 122)
						char_list.append(new_char)
						#print("old char is:", char, end="")
						#print("new char is:", new_char, end="")
					else:
						new_char = chr(ord(char)+key)
						#cyphered_txt += new_char
						char_list.append(new_char)
						#print(new_char, end="")
				else:
					#cyphered_txt += char
					char_list.append(char)
					#print(char, end="")
			#print()
			new_sentence = ''.join(char_list)
		w.write(new_sentence)
		print("Initial Message:", line)
		print("Key: ", key)
		print("Cypered Message:",new_sentence)
	w.write("\nThe key of the month is the sons of rome")
	f.close()
	w.close()
	return new_sentence

	#create a loop that goes through the string 
	#for each character
	#using the key, increase the number according to the ascii code

if __name__== "__main__":
        main()
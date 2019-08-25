def main():
	f= open("akademyai.txt","r")
	f1 =f.readlines()
	for line in f1:
		if line =='\n':
			print("found an empty line")
		else:
			for e in line.split():
				print(e)

	f.close()

if __name__== "__main__":
	main()
def main():
	f= open("akademyai.txt","r")
	if f.mode =='r':
		contents =f.read()
		print("Reading:", contents)
	f.close()

if __name__== "__main__":
    main()
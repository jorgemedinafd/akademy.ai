def main():
	f = open("akademyay.txt","a+")
	for i in range(5):
		f.write("Appending a new line %d \n" % (i+1))
	f.close()

if __name__== "__main__":
		main()
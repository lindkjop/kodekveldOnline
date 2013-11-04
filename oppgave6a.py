
def letterCount(inputString):
	lettersCount = {}
	for letter in inputString :
		if(letter in lettersCount) :
			lettersCount[letter] += 1
		else :
			lettersCount[letter] = 1
	print lettersCount			


#letterCount("Testtesttest")

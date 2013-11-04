import oppgave8

def findBiggestList(list) :
	biggestList = []
	sum = 0
	for l in list : 
		tempSum = oppgave8(l)
		if tempSum > sum:
			biggestList = l
			sum = tempSum
	return biggestList

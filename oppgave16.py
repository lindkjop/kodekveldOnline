################################################
#oppgave 16
################################################
def sortList(list):
	unsorted = True
	while unsorted:
		unsorted = False
		for x in range(0,len(list)-1):
			if(list[x]> list[x+1]):
				tmp = list[x+1]
				list[x+1] = list[x]
				list[x] = tmp
				unsorted = True
	return list

list = [5,3,7,9,2,1]
print(sortList(list))



##############################################
#oppgave 15
##############################################
def difftong(sentence):
	list = sentence.split(' ')
	longest = ""
	
	for x in range(0,len(list)):
		if hasDifftong(list[x]) and len(list[x])>len(longest):
			longest = list[x]
	return longest

def hasDifftong(word):
	vowels = 'aeoiyu'
	for x in range(0,len(word)-1):
		if((vowels not in word[x]) and (vowels not in word[x+1])):
			return True

	return False


print(difftong('hei deg heia'))

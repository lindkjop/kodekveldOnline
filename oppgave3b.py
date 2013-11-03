i = 1
j = 1
while (i <= 10) :
	string = " "
	while (j <= 10) :
		string += str(i*j) + " "
		j = j + 1
	#print "\n"
	j = 1
	i = i + 1
	print string

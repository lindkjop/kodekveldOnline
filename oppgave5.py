import datetime
now = datetime.datetime.now()
inputNumber = int(raw_input("Skriv inn foedselsaarstall : "))
currentYear = now.strftime("%Y")
legalYear = inputNumber + 18

if legalYear <= currentYear :
	print "Kunden kan kjoepe alkohol"
else :
	print "Kunden er for ung"

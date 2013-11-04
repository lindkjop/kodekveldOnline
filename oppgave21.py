# coding=utf-8

# parseMath() funksjonen tar inn en mattestreng av typen "485*(347/12)+45-3.5" og returnerer svaret.
# Skrevet av Nikolai Krill.
def parseMath(input):
	# Starter med å løse opp paranteser
	nestLevel = 0 # Hvor mange paranteser vi befinner oss i
	startI = -1 # Indeksen til startparantesen
	i = 0
	while i < len(input):
		c = input[i]
		if c == "(":
			if nestLevel == 0:
				startI = i
			nestLevel += 1
		elif c == ")":
			nestLevel -= 1
		if nestLevel == 0 and startI != -1:
			# Vi har funnet et gyldig parantessett
			# Bytt ut parantes substringen med resultat fra rekursivt kall
			substring = input[startI+1:i]
			replacement = parseMath(substring)
			input = input[:startI] + str(replacement) + input[i+1:]
			# i forminskes med differansen på lengden til de to strengene
			i -= (i+1-startI)-len(str(replacement))
			startI = -1
		if nestLevel < 0:
			# Vi har funnet et lukkeparantes for mye, returner error
			return float("nan")
		i += 1
	if nestLevel != 0:
		# Vi ikke funnet like mange åpningsparanteser som lukkeparanteser, returner error
		return float("nan")

	# Nå er alle parantesene løst opp og byttet ut med resultatet av rekursivt kall.
	
	# Splitt strengen på pluss og minus først. Ved å gjøre dette sørger vi for at
	# ganging og deling skjer før pluss og minus
	for i in range(0, len(input)):
		c = input[i]
		if c == "+":
			# Vi har funnet et pluss. Returner rekursivt kall av det før plussen + det etter plussen.
			return parseMath(input[:i])+parseMath(input[i+1:])
		if c == "-":
			# Vi har funnet et minus. Dette kan enten bety at vi skal subtrahere eller at det er snakk om
			# et negativt tall. Sjekker derfor om minusen kommer etter et tall. Hvis den kommer etter et tall
			# så gjør vi det om til addisjon og beholder minusen. Hvis ikke så gjør vi ingenting.
			if i > 0:
				previous = ord(input[i-1]);
				if (previous >= ord("0") and previous <= ord("9")) or previous == ord("."):
					# Minusen er etterfulgt av et tall og da skal vi subtrahere. Returnerer rekursivt kall
					# av det før minusen + rekursivt kall av minusen og det etter.
					# Vi bruker addisjon istedet for subtraksjon slik at fortegnene til tallene i andre del av
					# uttryket beholdes riktig.
					return parseMath(input[:i])+parseMath(input[i:])

	# Nå eksisterer det ikke noe pluss eller minus (annet enn fortegn) i uttrykket, og vi kan gjøre ganging og deling.
	for i in range(0, len(input)):
		c = input[i]
		if c == "*":
			# Vi har funnet et gangetegn. Returner rekursivt kall av det før gangetegnet * det etter gangetegnet.
			return parseMath(input[:i])*parseMath(input[i+1:])
		if c == "/":
			# Vi har funnet et deletegn. Returner rekursivt kall av det før deletegnet / det etter deletegnet.
			# Sjekk at nevneren ikke er 0.
			divisor = parseMath(input[i+1:])
			if divisor == 0:
				return float("nan")
			return parseMath(input[:i])/divisor

	# Nå eksisterer det kun en enkel verdi i uttrykket. Parse dette som en float og returner.
	return float(input)

# Noen tester for å passe på at alt fungerer.
assert parseMath("5*2-1") == 9
assert parseMath("5*2-1+1") == 10
assert parseMath("-5*3/-4") == 3.75
assert parseMath("45.3-(-35*0.2+7-(5+2)/(1.0-6))+5") == 48.9
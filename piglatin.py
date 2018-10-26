def encode(userInput):
	lstInput = userInput.split()
	vowel = ("aeiouy")
	for i in range (len(lstInput)):
		if lstInput[i][0] in vowel:
			lstInput[i] = lstInput[i] + "yay"
		else:
			for j in range(len(lstInput[i])):
				if lstInput[i][j] in vowel:
					lstInput[i] = lstInput[i][j:] + lstInput [i][:j] + "ay"
					break
	
	return (" ".join(lstInput)).lower()

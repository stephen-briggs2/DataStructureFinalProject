from collections import defaultdict
def Cichelli(sortingString): #Algorithm to hash the string using cichelli's algorithm
	import operator #Used when retrieving the largest value of a dictionary
	from sets import Set #Used when counting the number of unique elements in the array
	from collections import defaultdict
	sortingArray = [] #Empty array to store the individual words of the file
	sortingString = sortingString.lower() #Makes the string all lowercase letters

	for i in sortingString.split(): #loops through each individual word of the string and adds them into the array
		sortingArray.append(i) #Appends the current word to the array
	
	sortingSet = Set(sortingArray)
	sortingArray = []
	for i in sortingSet:
		sortingArray.append(i)


	tableLength = len(Set(sortingArray)) #Creates a Set object to count the number of unique items in the array and sets that length to tableLength

	letterCount = {} #Create an empty dictionary to keep track of letters
	for i in sortingArray: #loops through each word in the array to get a letter count
		hold = i #Store the current word in hold
		hold2 = hold[0] #Store the first character in hold2
		if hold2 in letterCount: #Checks to see if the letter is already in the dictionary
			letterCount[hold2] += 1 #If it is, increment the count
		else:
			letterCount[hold2] = 1 #If it's not, add an entry
			
		hold2 = hold[-1] #Stores the last character into hold2
		
		if hold2 in letterCount: #See previous condition statement
			letterCount[hold2] += 1
		else:
			letterCount[hold2] = 1

	sortedArray = []
	for x in range(len(sortingArray)): #Loops through the length of the array
		biggestWord = "" #Sets or resets the value of biggestWord
		biggestValue = 0 #Sets/resets the value of biggestValue
		for i in sortingArray: #Loops through every element in the array
			currentValue = 0 #Sets/resets the value of currentValue
			currentLetter = i[0] #Extract the first letter into currentLetter
			currentValue += letterCount[currentLetter] #add the value of the key to currentValue
			currentLetter = i[-1] #Extract the last letter
			currentValue += letterCount[currentLetter] #add the value of the key to currentValue
			if currentValue > biggestValue:
				biggestWord = i
				biggestValue = currentValue
		
		sortingArray.remove(biggestWord)
		sortedArray.append(biggestWord)
						
	return sortedArray

def search(wordlist, gDictionary, tablelength, cichelliDict): #Search function to find an element's cichelli value
	result = False
	theMax = 5 #The maximum number of times the algorithm will try for a result
	if wordlist == []: #If all the words have been found...
		return None #Exit the program
	word = wordlist[0] #Set the value of word to the first element in the list
	wordlist = wordlist[1:] #Remove the first element in the list
	if (word[0] in gDictionary) & (word[-1] in gDictionary): #If both the first and last letter of a word already have a g-value...
		result, value, gDictionary = cichelliTry(word, gDictionary[word[0]], gDictionary[word[-1]], tablelength, gDictionary) #See if the value works
		if result: #If the value works...
			search(wordlist, gDictionary, tablelength, cichelliDict) #move on to the next value
			wordlist.insert(0, word) #replace the value at the top of the list
		
	elif (word[0] not in gDictionary) & (word[-1] not in gDictionary): #If neither letters have a g-value...
		for n in range(theMax): #Try 4 times for the first letter
			for m in range(theMax): #Try 4 times for the last letter
				result, value, gDictionary = cichelliTry(word, n, m, tableLength, gDictionary) #See if the current g-values work

				if result: #if they do...
					search(wordlist, gDictionary, tablelength, cichelliDict) #Move on to the next word
					if len(cichelliDict) == tablelength:
						break
			if len(cichelliDict) == tablelength:
				break

		if result:
			wordlist.insert(0, word) #replace the value at the top of the list
			
		
	elif (word[0] not in gDictionary) & (word[-1] in gDictionary): #If the first letter does not have a g-value but the last letter does...
		for n in range(theMax): #try 4 times for the first letter
			result, value, gDictionary = cichelliTry(word, n, gDictionary[word[-1]], tablelength, gDictionary) #See if the current g-values work
			if result: #If they do...
				search(wordlist, gDictionary, tablelength, cichelliDict) #Try the next word
				if len(cichelliDict) == tablelength:
					break
		if result:
			wordlist.insert(0, word) #Replace the word at the top of the list

	elif word[-1] not in gDictionary: #If the last letter does not have a g-value...
		for n in range(theMax): #try 4 times
			result, value, gDictionary = cichelliTry(word, gDictionary[word[0]], n, tablelength, gDictionary) #See if the current g-values work
			if result: #if they do...
				search(wordlist, gDictionary, tablelength, cichelliDict) #Move on to the next word
				if len(cichelliDict) == tablelength:
					break
		if result:
			wordlist.insert(0, word) #Replace the current value





def cichelliTry(word, firstLetterValue, lastLetterValue, tableLength, gDictionary): #Attempts to see if the current g-values work
	value = cichelliValue(word, firstLetterValue, lastLetterValue, tableLength) #Calls the function that will retrieve the value
	if value in cichelliDict.values(): #Checks if the value has been used
		return False, -1, gDictionary #If the value has been used return false and -1
	else: #If it's unused...
		gDictionary[word[0]] = firstLetterValue #Set the g-value for the first letter
		gDictionary[word[-1]] = lastLetterValue #Set the g-value for the last letter
		cichelliDict[word] = value
		return True, value, gDictionary #Return that it worked, what the value is, what values are now used up, and what the current g-values are



def cichelliValue(word, firstLetterValue, lastLetterValue, tableLength): #Calculates the hash values
	return (len(word) + firstLetterValue + lastLetterValue) % tableLength  #returns the hash value


def runLength(wordString):
	import string
	wordString = wordString.lower() + " "
	newString = ""
	letterCount = 1
	for i in range (len(wordString)-1):
		
		if wordString[i] == wordString[i+1]:
			letterCount += 1
		else:
			newString = newString + wordString[i] + str(letterCount)
			letterCount = 1
	print newString 

thisString = "This is a string wweeeee neeeed similarrrritiees"
runLength(thisString)

wordString = "Calliope clio erato euterpe melpomene polyhymnia terpsichore thalia urania" #Current word string
wordlist = Cichelli(wordString)
print wordlist
cichelliDict = defaultdict(int)
gDictionary = {} #Starts an empty dicitonary for the g-values
 #Starts an empty list for the cichelli values
tableLength = len(wordlist) #Finds out the length of the list
search(wordlist, gDictionary, tableLength, cichelliDict) #Starts the program
for i in cichelliDict.items():
	print i


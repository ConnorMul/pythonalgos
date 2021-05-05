# TWO NUMBER SUM 

def twoNumberSum(array, targetSum):
	numHash = {}
	for num in array:
		complement = targetSum - num
		
		if complement in numHash:
			return [num, complement]
	
		numHash[num] = True
		
	return []

def twoNumberSum(array, targetSum):
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
            
    return []

# VALIDATE SUBSEQUENCE

def isValidSubsequence(array, sequence):
    arrayIdx = 0
    seqIdx = 0
	
    while arrayIdx < len(array) and seqIdx < len(sequence):
		if array[arrayIdx] == sequence[seqIdx]:
			seqIdx += 1

		arrayIdx += 1

    return seqIdx == len(sequence)

# SORTED SQUARED ARRAY

def sortedSquaredArray(array):
    resultArray = []

    for num in array:
		resultArray.append(num * num)
    resultArray.sort()
    return resultArray

# NONCONSTRUCTIBLE CHANGE

def nonConstructibleChange(coins):
    cantConstruct = 0
    coins.sort()
    i = 0
    while i < len(coins):
		if coins[i] > cantConstruct + 1:
			return cantConstruct + 1

		cantConstruct += coins[i]
		i += 1

    return cantConstruct + 1

# MINIMUM WAITING TIME

def minimumWaitingTime(queries):
    queries.sort()
    timeToExecute = 0

    for idx, time in enumerate(queries):
		queriesLeft = len(queries) - (idx + 1)
		timeToExecute += time * queriesLeft

    return timeToExecute

# CLASS PHOTOS

def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()
    lastIdx = len(redShirtHeights) - 1
	
    if redShirtHeights[lastIdx] > blueShirtHeights[lastIdx]:
		backRow = redShirtHeights
		frontRow = blueShirtHeights
    else:
		frontRow = redShirtHeights
		backRow = blueShirtHeights
	
    i = 0
    while i < len(frontRow):
		if frontRow[i] >= backRow[i]:
			return False
		i += 1
	
    return True


# TANDEM BICYCLE

def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
	redShirtSpeeds.sort()
	blueShirtSpeeds.sort()
	
	if not fastest:
		reverseArray(redShirtSpeeds)
	
	totalSpeed = 0
	for idx in range(len(redShirtSpeeds)):
		rider1 = redShirtSpeeds[idx]
		rider2 = blueShirtSpeeds[len(blueShirtSpeeds) - idx - 1]
		totalSpeed += max(rider1, rider2)
	
    return totalSpeed

def reverseArray(array):
	start = 0
	end = len(array) - 1
	while start < end:
		array[start], array[end] = array[end], array[start]
		start += 1
		end -= 1
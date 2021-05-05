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
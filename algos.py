# TWO NUMBER SUM 

def twoNumberSum(array, targetSum):
	numHash = {}
	for num in array:
		complement = targetSum - num
		
		if complement in numHash:
			return [num, complement]
	
		numHash[num] = True
		
	return []
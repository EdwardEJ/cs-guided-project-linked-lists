def smallestDifference(arrayOne, arrayTwo):
	arrayOne.sort()
	arrayTwo.sort()
	indxOne = 0
	indxTwo = 0
	smallest = float('inf')
	current = float('inf')
	smallestPair = []
	
	while indxOne < len(arrayOne) and indxTwo < len(arrayTwo):
		firstNum = arrayOne[indxOne]
		secondNum = arrayTwo[indxTwo]
		if firstNum < secondNum:
			current = secondNum - firstNum
			indxOne += 1
		elif secondNum < firstNum:
			current = firstNum - secondNum
			indxTwo += 1
		else:
			return [firstNum, secondNum]
		if smallest > current:
			smallest = current
			smallestPair = [firstNum, secondNum]
	return smallestPair
	
print(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))
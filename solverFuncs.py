def get_cages():
    numCages = int(input('Number of cages: '))
    cageCount = 0
    cages = []
    for num in range(numCages):
        cage = input('Cage number %d: ' % (cageCount)).split()
        cage = [int(num) for num in cage]
        cages.append(cage)
        cageCount += 1
    return cages
        
def check_rows_valid(puzzle):
    for row in puzzle:
        for num in row:
            numCount = row.count(num)
            if numCount > 1 and num != 0:
                return False
    return True  
          
def check_columns_valid(puzzle):
    for col in range(len(puzzle)):
        seen = []
        for row in range(len(puzzle)): #looks through each column, then goes down a row
            seen.append(puzzle[row][col])
        for num in seen:
            if seen.count(num) > 1 and num != 0: #same as row function
                return False
    return True
            
def check_cages_valid(puzzle, cages):
    for subCage in cages: #subCages are the 'sublists' in the user input cages
        cageSum = 0
        checkList = []
        for num in subCage[2:len(subCage)]: #for each entry in user's input, index 2 and beyond
            #assigning each cell number to a row and column position
            rowNum = num // 5 
            colNum = num % 5
            checkList.append(puzzle[rowNum][colNum])
        for i in range(len(checkList)): #add up elements of list to input total
            cageSum += checkList[i]
        #if there are zeroes in the cage and whether or not sum is equal to 0th index of input list
        if checkList.count(0) >= 1: #if the sum of cage is greater than what the user put in
            if cageSum >= subCage[0]:
                return False
            else:
                continue #continue checking counting entries in checkList
        elif cageSum != subCage[0]:
            return False
    return True
            
def check_valid(puzzle, cages): #if the 3 functions satisfy the base rules of calcudoku 
    if check_rows_valid(puzzle) and check_columns_valid(puzzle) and check_cages_valid(puzzle, cages) == True:
        return True
    else:
        return False

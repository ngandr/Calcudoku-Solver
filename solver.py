from solverFuncs import *

def main():
    userInputCage = get_cages()
    Puzzle = [[0,0,0,0,0],
              [0,0,0,0,0],
              [0,0,0,0,0],
              [0,0,0,0,0],
              [0,0,0,0,0]]
    row = col = checks = backtracks = 0
    while row < 5: #while the calculations still in puzzle 5 x 5
        Puzzle[row][col] += 1 #incrementing at current spot
        checks += 1 #increment checks 
        puzzleValid = check_valid(Puzzle, userInputCage)
        if puzzleValid == True: #if all base calcudoku rules are met
            col += 1 
            if col == 5: #move down a row and restart columns
                col = 0
                row += 1
        elif puzzleValid == False:
            while Puzzle[row][col] == 5:#hitting maximum value of puzzle
                Puzzle[row][col] = 0 #keep doing this when spot equals 5
                col -= 1 #and assign that spot back to zero, moving back
                backtracks += 1 #increment backtracks
                if col < 0: #go back one row when col hits the beginning of list
                    col = 4 #a row ends at 4
                    row -= 1#go back one row
                    
    print()
    print('---Solution---')
    print()
    for i in range(len(Puzzle)):
        print('%d %d %d %d %d' % (Puzzle[i][0], Puzzle[i][1], Puzzle[i][2], Puzzle[i][3], Puzzle[i][4]))
    print()
    print('checks: %d backtracks: %d' % (checks, backtracks))

if __name__ == '__main__':
    main()

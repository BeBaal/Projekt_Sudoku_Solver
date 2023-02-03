import pandas as pd

# ToDo Implement time keeping
# ToDo reading from table
# ToDo implement parallel processing


SUDOKU_MATRIX = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 0, 0]]

SUDOKU_MATRIX = pd.DataFrame(SUDOKU_MATRIX)



def validation(row,column,number_to_insert):

    # check row for number
    if (SUDOKU_MATRIX.iloc[row,:].isin([number_to_insert]).sum()):
        return False
    
    # check column for number
    if (SUDOKU_MATRIX.iloc[:,column].isin([number_to_insert]).sum()):
        return False
    
    # check quadrant for number
    row_group = (row // 3) * 3
    column_group = (column // 3) * 3
    
    # loop over quadrant
    for i in range(3):
            for j in range(3):
                if SUDOKU_MATRIX.iloc[row_group + i,
                                      column_group + j] == number_to_insert:
                    return False
    
    return True


def main():

    # loop over table
    for rows in range(9):

        for columns in range(9):
            
            # check if cell is empty
            if SUDOKU_MATRIX.iloc[rows, columns] == 0:

                # try all numbers
                for number in range(1,10):
                    if  validation(rows, columns, number):
                        SUDOKU_MATRIX.iloc[rows, columns] = number
                        main()
                        SUDOKU_MATRIX.iloc[rows, columns] = 0
                return
            
    print(SUDOKU_MATRIX) 
    input("More?")
                
    
    
main()
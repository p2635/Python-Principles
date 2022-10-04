# Tictactoe Input (https://pythonprinciples.com/challenges/Tic-tac-toe-input/)
# Function takes a single string of length 2
# consisting of an uppercase letter and a digit.
# I disagree with the website, it should be called get_col_row. 'A1' is clearly in the format column-row and not row-column.
def get_row_col(string):
    
    # Assuming A-C only board
    mydict = {
        "A": 0,
        "B": 1,
        "C": 2
    }
    column = mydict[string[0]]
    row = int(string[1])-1
    return (row, column)

# This should be (0, 2)
print(get_row_col("A3"))

# This should be (0, 1)
print(get_row_col("B1"))

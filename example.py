import numpy as np

connect_four = [[0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 2, 0, 0, 0],
                [0, 0, 0, 2, 1, 0, 0],
                [0, 0, 0, 2, 1, 0, 0],
                [0, 0, 0, 2, 1, 1, 0]]

connect_four = np.array(connect_four)
print(connect_four[2, 3])

def check_four(row):
    
    return 

for row in connect_four:
    # Check whether there is a four-in-a-row in each row
    print(row)

for row in connect_four.T:
    # Check whether there is a four-in-a-row in each column
    print(row)
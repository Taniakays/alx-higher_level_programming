#!/usr/bin/python3
def square_matrix_sample(matrix=[]:
        #create a new matrix to store the squared
        squared_matrix = []

        # Iterate over each row in the input matrix
        for row in matrix:
        #Create a new row for the squared values
        squared_row = []

        #Iterate over each element in the row and square the value
        for element in row:
        squared_value = element ** 2
        squared_row.append(squared_value)

        # Add the squared row to the new matrix
        squared_matrix.append(squared_row)

        return squared_matrix

        #Example usage:
        input_matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]

        ]

        result = square_matrix_simple(input_matrix)
        print(result)

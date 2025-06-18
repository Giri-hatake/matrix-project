import numpy as np

class Matrix:

    # creating a method for getting the inputs :

    def __init__(self):
        self.rows1 = (int(input("Enter the row of matrix A:")))
        self.col1 = (int(input("Enter the column of matrix A:")))
        self.rows2 = (int(input("Enter the row of matrix B:")))
        self.col2 = (int(input("Enter the column of matrix B:")))
        

        self.matrix_A = [] 
        print("Enter the elements of matrix A by row-wise:")

        for i in range(self.rows1):   
            row = []
            for j in range(self.col1):
                row.append(int(input(f"Matrix_A{[i+1]}{[j+1]} = ")))    # user input for rows
            self.matrix_A.append(row) 

        self.matrix_B = []
        print("Enter the elements of matrix A by row-wise:")

        for i in range(self.rows2):   
            row = []
            for j in range(self.col2):
                row.append(int(input(f"Matrix_B{[i+1]}{[j+1]} = ")))    
            self.matrix_B.append(row)  

        print("\nThe matrix of A is:")

        # print(self.matrix_A)

        for i in range(self.rows1):
            for j in range(self.col1):
                print(self.matrix_A[i][j], end=" ")
            print()

        print("\nThe matrix of B is:")

        for i in range(self.rows2):
            for j in range(self.col2):
                print(self.matrix_B[i][j], end=" ")
            print()


    def add_sub(self):
      
        if self.rows1 == self.rows2 and self.col1 == self.col2:

            # Matrix_addition
            add_res = [[self.matrix_A[i][j] + self.matrix_B[i][j] for j in range(self.col1)] for i in range(self.rows1)]

            # Matrix subtraction
            sub_res = [[self.matrix_A[i][j] - self.matrix_B[i][j] for j in range(self.col1)] for i in range(self.rows1)]

            print("Matrix Addition:")
            for row in add_res:
                print(row)

            print("\nMatrix Subtraction:")
            for row in sub_res:
                print(row)
        else:
            print("Matrix addition and Subtraction is not possible")

    # creating a method for multiplication

    def mul(self):
        if self.col1 == self.rows2:
            self.result=np.dot(self.matrix_A,self.matrix_B)
            print("The result for multiplication:\n",self.result)
            
            
        else:
            print("Matrix multiplication is not possible")



    def inverse(self):
        try:
            matrix_inverse=np.linalg.inv(np.array(self.result))
            print("The Result for the inverse matrix is: \n ",matrix_inverse)
        
        except:
            print("The matrix is a singular matrix \n SO,Matrix inverse is not possible!!")


# creating a sub classes:
class Calculation(Matrix):
    def inverse_A(self):

        if self.rows1 == self.col1:
            self.result_A_inverse=np.linalg.inv(self.matrix_A)
            print("inverse of matrix_A:\n",self.result_A_inverse)
        else:
            print("matrix inverse is not possible...\n since,The matrix A is not a square matrix!!")

    def mul_A_A_inverse(self):
        try:
            unit=np.dot(self.matrix_A ,self.result_A_inverse)
            print("multiplication of matrix [A][A_inverse]:\n",unit)

        
        except:
            print("matrix inverse is not possible ")


C=Calculation()

C.add_sub()
C.mul()
C.inverse()
C.inverse_A()
C.mul_A_A_inverse()
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 23:14:01 2021

@author: arnab19
"""

NUM_ROWS = 25
NUM_COLS = 25

# construct a matrix
my_matrix = []
for row in range(NUM_ROWS):
    new_row = []
    for col in range(NUM_COLS):
        new_row.append(row * col)
    my_matrix.append(new_row)
 
# print the matrix
for row in my_matrix:
    print(row)

summ = 0    
for i in range(NUM_ROWS):
    summ = summ + my_matrix[i][i]
print(summ)    
print({0 : [], 1 : [1], 2 : [2, 2], 3 : [3, 3, 3]})
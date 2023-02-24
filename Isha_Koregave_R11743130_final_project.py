#Isha Koregave | R11743130 | Project | 11/30/2022
# This program recieves the path to the input file as an argument containing the starting cellular matrix. Depending on certain conditions the cellular matrix updates its elements for every step. This program will store the 100th step of the cellular matrix in the output file specified by the commnad line argument

import argparse
import sys
import os
from multiprocessing import Pool

#argument parser for command line
parser = argparse.ArgumentParser()
parser.add_argument("-i", dest='input', type=str, required=True)
parser.add_argument("-o", dest="output", type=str, required=True)
parser.add_argument("-t", dest="thread", type=int, default=1)
args = parser.parse_args()

print("Project :: R11743130")

#validating number of threads
if (args.thread > 0):
  threadcount = args.thread
  #print(threadcount)
else:
  print("Thread count should be greater than 0")
  exit(2)

#validating input file
if (os.path.exists(args.input)):
  matrix = open(args.input, "r")
else:
  print("Entire file path must exist")
  exit(3)

#checking if matrix only contains "+" and "-"
invalid_char = 0
while 1:
  char = matrix.read(1)
  if char != '\n' and char != "+" and char != "-":
    if not char:
      #print("EOF")
      break
    else:
      print("this is not valid char", char)
      invalid_char = 1
      break
if invalid_char == 1:
  exit(1)

#reading matrix from input file and storing as 2d array
matrix = []
with open(args.input) as textFile:
  for line in textFile:
    row_list = list(line.strip())
    #if new lines (empty) do not append to matrix
    if row_list:
      matrix.append(row_list)

#get dimensions of matrix
no_of_rows = len(matrix)
no_of_cols = len(matrix[0])


#returns number of alive neighbors for a element in the matrix
def count_alive(row, col):
  count = 0
  for i in range(row - 1, row + 2):
    for j in range(col - 1, col + 2):
      if i == no_of_rows:
        i = 0 #since right neighbor of last element in a row is the first element of that row
      if j == no_of_cols:
        j = 0 #since bottom neighbor of last element in a column is the first element of that column
      if (i == row and j == col):
        continue
      if matrix[i][j] == "+":
        count = count + 1
  return count


#create new matrix same size as given matrix
new_matrix = [[0 for _ in range(no_of_cols)] for _ in range(no_of_rows)]


#update new matrix accoridng to its alive neighbors
def update(R, C):

  alive = count_alive(R, C)
  
  if matrix[R][C] == "+":
    if alive in [2, 4, 6]:
      new_matrix[R][C] = "+"
    else:
      new_matrix[R][C] = "-"

  else:
    if alive in [2, 3, 5, 7]:
      new_matrix[R][C] = "+"
    else:
      new_matrix[R][C] = "-"
  return new_matrix[R][C]


#get one dimensional list of all index positions(vertices) of matrix 
def list_of_vertices():
  index_position = []
  for R in range(no_of_rows):
    for C in range(no_of_cols):
      index_position.append((R, C))
  return index_position
  
#convert one dimensional list to a 2d array/matrix
def one_d_list_to_matrix(Matrix, List):
  Matrix = [
    List[i:i + no_of_cols]
    for i in range(0, len(List), no_of_cols)
  ]
  return Matrix


#rewrite original contents of matrix 
def rewrite_matrix(list_to_matrix):
  for row in range(no_of_rows):
      for column in range(no_of_cols):
        matrix[row][column] = list_to_matrix[row][column]

#to get 100th step of matrix, use parrallelization
for i in range(100):
  with Pool(threadcount) as p:
    one_d_list = p.starmap(update, list_of_vertices())
    
    #created matrix to store the above result which is a one dimensional list
    list_to_matrix = []
    list_to_matrix = one_d_list_to_matrix(list_to_matrix, one_d_list)

    #rewrite the original matrix by replacing it with above list_to_matrix 
    rewrite_matrix(list_to_matrix)

#writing matrix to output file after validating it
if (args.output):
  with open(args.output, 'w') as testfile:
    for row in matrix:
      testfile.write(''.join([str(a) for a in row]) + '\n')
else:
  print("Directories in the file path must exist")
  exit(4)

sys.stdout.close()


# -*- coding: utf-8 -*-
"""CS301_a4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1USiKqyl0EYh_Splz5-ANEUXUyDEyNW9w
"""

# Ahmet Bilal Yildiz

# Agricultural Robot problem

def MW(farm, maxFarm, i, j):

  if maxFarm[i-1][j-1] != -1: #if the max weed of the current is already calculated return the value

    return maxFarm[i-1][j-1]

  elif i == 1 and j ==1:

    maxFarm[i-1][j-1] = farm[i-1][j-1] #if i and j = 1, then fill the cell 1 if weed occurs or 0 if weed does not occur
    return maxFarm[i-1][j-1]

  elif i == 1: #if i = 1, then just take the max of left cell
    maxFarm[i-1][j-1] = MW(farm, maxFarm,i, j-1) + farm[i-1][j-1]
    return maxFarm[i-1][j-1]

  elif j == 1: #if j = 1, then just take the max of the upper cell
    maxFarm[i-1][j-1] = MW(farm, maxFarm,i-1, j) + farm[i-1][j-1]
    return maxFarm[i-1][j-1]
    
  else:

     maxFarm[i-1][j-1] =  max(MW(farm, maxFarm, i, j-1), MW(farm, maxFarm, i-1, j)) + farm[i-1][j-1] # if i and j != 1, then fill the cell with maximum of upper and lefter cell + 1/0 whether weed exits or not
     return maxFarm[i-1][j-1]


def PF(farm, maxFarm):

  path_list = [];

  i = len(farm) 
  j = len(farm[0]) 

  if i == 0 or j == 0:
    print("Error: There is no cell in the farm")
  
  else:

    path_list.append((i,j))
    MW(farm, maxFarm, i, j) # MW fills all the maxFarm matrix with corresponding max weed values

    while not (i == 1 and j == 1):

      if i == 1: #if we are in the upper corner just take the max of left
        path_list.append((i,j-1))
        j = j-1

      elif j == 1:
        path_list.append((i-1,j))
        i = i-1

      elif MW(farm, maxFarm, i, j-1) > MW(farm, maxFarm, i-1, j):
        path_list.append((i,j-1))
        j = j-1

      else:
        path_list.append((i-1, j))
        i = i-1

    print("Path contains max number of weeds: ")
    for i in range(len(path_list)):
      print(path_list[len(path_list)-i-1])

def findPath(given_area):

  maxFarm =[[-1 for _ in range(len(given_area[0])) ] for _ in range((len(given_area)))] #initilaizing the maxFarm
  PF(given_area, maxFarm) #call the PF to find and return path

#benchmark suite for Correctness
import matplotlib.pyplot as plt
import numpy as np
import time

################# 
#blackbox testing
#--- eceptions ---
################# 

#1 an empty matrix
matrix1 = [[]]

#2 a matrix that consists only 1's
matrix2 = [
          [1,1,1],
          [1,1,1],
          [1,1,1]]

#3 a matrix that consists only 0's 
matrix3 = [
          [0,0,0],
          [0,0,0],
          [0,0,0]]

#4 a matrix that has 1xn structure
matrix4 = [[0,1,1,0,1,0]]

#5 a matrix that has nx1 structure

matrix5 = [[0],
           [1],
           [1],
           [0],
           [1]]

#################          
#whitebox testing
#################  


#6 a 5x6 matrix (the matrix in the homework document)
matrix6 = [
          [1, 0, 1, 0, 0, 0],
          [0, 1, 0, 1, 0, 0],
          [0, 1, 1, 0, 0, 0],
          [0, 0, 0, 0, 1, 0],
          [1, 0, 3, 0, 0, 1]]

#7 a 6x8 random matrix 
matrix7 = [
          [1, 1, 1, 1, 0, 1, 1, 0, 0, 0],
          [0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
          [0, 0, 1, 1, 0, 1, 0, 0, 1, 1],
          [0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
          [0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
          [1, 1, 1, 1, 0, 1, 1, 1, 1, 1]]
#8 a 15x10 matrix
matrix8 = [
          [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
          [0, 1, 1, 1, 0, 0, 0, 1, 0, 0],
          [1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
          [1, 0, 1, 1, 0, 1, 0, 0, 1, 1],
          [1, 0, 0, 0, 0, 0, 1, 1, 1, 0],
          [0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
          [1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
          [0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
          [1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
          [0, 1, 0, 1, 0, 0, 1, 0, 0, 1],
          [0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
          [0, 0, 1, 0, 0, 1, 1, 0, 1, 1],
          [1, 0, 0, 0, 1, 1, 1, 0, 1, 0],
          [1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
          [0, 0, 1, 0, 1, 0, 1, 0, 1, 0]]

test_list = [matrix1, matrix2, matrix3, matrix4, matrix5, matrix6, matrix7, matrix8]

#testing Correctness
for i in range(len(test_list)):
  matrix = test_list[i]
  print("Test Case",i+1, ": " )
  findPath(matrix)

#benchmark suite for Performance

#creating 5 random matrixes with different sizes and putting them to the performance_list
performance_list = []
for i in range(5):
  array = np.random.randint(2, size=(2 **(i+1), 2**(i+1)))
  performance_list.append(array)

#diplaying the performance_list
for i in range(len(performance_list)):
  print("performance matrix", i+1, "(",2 **(i+1), "x", 2**(i+1), ")", ":")
  print(performance_list[i])
  print()

#testing Performance #outputs 
#run all the matrixes and plot the graph of their running times
time_list =[]
for matrix in performance_list:
  t0= time.process_time()
  findPath(matrix)
  t1 = time.process_time() - t0
  time_list.append(t1)

input_list = [2,4,8,16,32]

#performance test #plotting the graph
plt.plot(input_list, time_list)
plt.xlabel('size of the row and cols of matrix ')
plt.ylabel('running times in(s)')
plt.title('Performance Test Running Times')
plt.show()
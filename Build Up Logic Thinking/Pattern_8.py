#  *********
#   *******
#    *****
#     ***
#      *

N=int(input())
for row in range(N):
  for col in range(row):
    print(" ",end="")
  for col in range(2*N-(2*row+1)):
    print("*",end="")
  print() 

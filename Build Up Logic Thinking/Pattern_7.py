#      *
#     ***  
#    *****
#   *******
#  *********

N=int(input())
for row in range(N):
  for col in range(N-row-1):
    print(" ",end="")
  for col in range(row*2+1):
    print("*",end="")
  print()

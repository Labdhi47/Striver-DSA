#   1 2 3 4 5
#   1 2 3 4
#   1 2 3 
#   1 2  
#   1 

T=int(input())
for row in range(T):
  for col in range(T-row):
    print(col+1,end=" ")
  print() 

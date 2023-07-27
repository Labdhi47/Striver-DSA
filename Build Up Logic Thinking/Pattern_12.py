# 1                 1
# 1 2             2 1
# 1 2 3         3 2 1
# 1 2 3 4     4 3 2 1
# 1 2 3 4 5 5 4 3 2 1

for i in range(N):
  space=2*(N-1)
  for j in range(i+1):
    print(j+1,end=" ")
  for j in range(space-(2*i)):
    print(" ",end=" ")
  for j in reversed(range(i+1)):
    print(j+1,end=" ")
    j-=1
  print()
              

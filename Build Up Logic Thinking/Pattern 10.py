#  * 
#  * * 
#  * * * 
#  * * * * 
#  * * * * *
#  * * * *
#  * * *
#  * *
#  *

N=int(input))
for i in range(1,N+1):
  print("* "*i,end="")
  print()
for j in range(1,N):
  print("* "*(N-j),end="")
  print()

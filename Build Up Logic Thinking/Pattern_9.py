#       *
#      * *
#     * * *
#    * * * *
#   * * * * *
#   * * * * *
#    * * * *
#     * * *
#      * *
#       *

N=int(input())
j=N-1
for i in range(1, N+1):
  print(" "*j, end="")
  print("* "*i)
  j=j-1
j=0
for i in range(N, 0, -1):
  print(" "*j, end="")
  print("* "*i)
  j=j+1

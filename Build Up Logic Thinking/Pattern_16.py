# A
# BB
# CCC
# DDDD
# EEEEE

v=65
for i in range(5):
  for j in range(i+1):
    print(chr(v),end="")
  v+=1
  print()

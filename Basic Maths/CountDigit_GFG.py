# Count Digits 

# N = 12
# Output: 2
# Explanation: 1, 2 both divide 12 evenly

N=int(input())
  count=0
  num=N
  while(N>0):
    last_digit=N%10
    N=N//10
    if last_digit!=0:
      if num%last_digit==0:
        count+=1
  return count

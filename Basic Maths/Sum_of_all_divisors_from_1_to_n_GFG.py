# Sum of all divisors from 1 to n

N=int(input())
count=0
for i in range(1,N+1):
  count+=i*(N//i)
return count    

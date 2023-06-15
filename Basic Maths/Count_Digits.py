#solution_1
N=int(input())
count=0
while(N>0):
    last_digit=N%10
    count=count+1
    N=N//10
    print(last_digit) 
print("The total digit is:",count) 

# solution_2
import math
T=int(input())
count=int(math.log10(T)+1)
# N//10 so log10(x) is taking or for example N//5 then you must take log5(x)
print(count) 

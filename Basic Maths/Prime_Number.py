# a whole number greater than 1 that cannot be exactly divided by any whole number other than itself and 1 (e.g. 2, 3, 5, 7, 11).

N=int(input())
count=0
for i in range(1,N+1):
    if N%i==0:
        count+=1
if count==2:
    print(f"{N} is the prime number.")
else:
    print(f"{N} is not a prime number.")            

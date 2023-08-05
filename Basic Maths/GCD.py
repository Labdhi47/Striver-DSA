#1
num1=int(input())
num2=int(input())
gcd=1
for i in range(1,min(num1,mun2)):
    if num1%i==0 and num2%i==0:
        gcd=i
print(gcd) 

#2
num1=int(input())
num2=int(input())
gcd=1
i=1
while(i<=num1 and i<=num2):
    if num1%i==0 and num2%i==0:
        gcd=i
    i+=1    
print(gcd)

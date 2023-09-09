def factorial(n):
 if n==0 or n==1:
   return (1)
 else:
     return (n*(n-1))
n=int(input("enter a number"))
fact=factorial(n)
print ("the factorial of",n,"is", fact)
def power_with_modules(a,b,c):
    result=1
    for i in range(b):
        result=(result*a)%c
    return result%c


a=int(input("Enter the Number A : "))
b=int(input("Enter the Number B : "))
c=int(input("Enter the Number C : "))
print(power_with_modules(a,b,c))
#Write a python script to print first 10 multiples of N
n=int(input("enter value of n to print 10 multiples of it : "))
for c in range(n,n*10+1,n):
    print(c,end=' ')

n=int(input())
sqar=n*n
s=0
c=0
while n>0:
    r=n%10
    s=s*10+r
    n//=10
a=s**2
while a>0:
    x=a%10
    c=c*10+x
    a//=10
if c==sqar:
    print("True")
else:
    print("False")
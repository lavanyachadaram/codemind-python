n=int(input())
I=list(map(int,input().split()))
s=sum(I)//len(I)
if s in I:
   print("True")
else:
   print("False")
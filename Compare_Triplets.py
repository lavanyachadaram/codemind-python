n=list(map(int,input().split()))
k=list(map(int,input().split()))
a=[]
v=0
q=0
for i in range(0,3):
  if(n[i]>k[i]):
     q+=1
  elif(n[i]<k[i]):
     v+=1
a.append(q)
a.append(v)
for j in range(len(a)):
  print(a[j],end=" ")
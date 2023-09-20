c=int(input())
nums=list(map(int,input().split()))
k=nums.count(0)
for i in range(k):
  nums.remove(0)
for j in range(k):
  nums.append(0)
print(*nums)
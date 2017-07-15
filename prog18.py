print("Enter start interval: ")
a=int(input())
print("Enter stop interval: ")
b=int(input())
for i in range(a,b+1):
  sum=0
  list=[]
  n=len(str(i))
  for j in str(i):
    list.append(int(j)**n)
  for j in list:
    sum+=j
  if sum==i:
    print(i)

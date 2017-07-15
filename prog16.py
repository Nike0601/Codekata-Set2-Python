print("Enter limit: ")
num=input()
for i in range(2,num):  
  p=1
  for j in range(2,i):
    if i%j==0:
      p=0
      break
  if p!=0:
      print(i)
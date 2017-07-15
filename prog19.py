print("Enter number: ")
num=int(input())
pdt=1
for i in range(1,num+1):
  pdt*=i
print(str(num)+"!= "+str(pdt))

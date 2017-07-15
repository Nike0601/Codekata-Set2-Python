print("Enter number: ")
num=int(input())
list=[]
sum=0
n=len(str(num))
for i in str(num):
  list.append(int(i)**n)
for i in list:
  sum+=i
print(sum)
if sum==num:
  print("Number is an armstrong number")
else:
  print("Number is not an armstrong number")

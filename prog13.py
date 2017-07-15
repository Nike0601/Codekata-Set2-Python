print("Enter number: ")
num=input()
p=1
for i in range(2,num):
  if num%i==0:
    print("Number is not a prime")
    p=0
    break

if p!=0:
  print("Number is a prime")
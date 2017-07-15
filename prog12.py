print("Enter number: ")
num=str(input())
num_rev=num[::-1]
if num==num_rev:
  print("The number is a palindrome")
else:
  print("The number is not a palindrome")

x = int(input("Enter the  Number" ))
if x==0:
	print("Number is palindrome")
while x!=0:
	int digit=0,int rev=0
	digit = x%10
	rev = rev * 10 + digit
	x= x//10
if x==rev:
	print("Number is palindrome")
else:
	print("Number is not Palindrome")


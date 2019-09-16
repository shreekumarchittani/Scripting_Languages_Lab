a = {}
while(True):
	print("Enter the reg no or -1 to exit")
	reg = int(input())
	if(reg==-1):
		break
	name = input()
	a[reg] = name
for k,v in a.items():
	if(k%2==0):
		print(a[k])		

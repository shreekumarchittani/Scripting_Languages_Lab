EvenList = []
OddList = []
while(True):	#make sure that t is always capital	
	print("Enter a string,-1 to exit")
	x = input()	#input() takes string as input
	if x=='-1':
		break
	else:
		if len(x)%2==0:
			EvenList.append(x)
		else:
			OddList.append(x)
print(EvenList)
print(OddList)					

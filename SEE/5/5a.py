def celsToKel(cel):
	return cel + 273
def celsToFarh(cel):
	far = 32 + (1.8 * cel)
	return far
print("Welcome to tempeature convertor")
while(True):
	print("Enter NO to exit,anything for conversion")
	x = input()
	if(x=="NO"):
		break
	else:
		print("1:Celsius to Kelvin 2:Celsius to Farheneit")
		choice = int(input())
		cel = int(input("Enter temperature in celsius"))
		if(choice==1):
			print("Celsius to Kelvin: ",celsToKel(cel))
		else:
			print("celsius to farheneit: ",celsToFarh(cel))	

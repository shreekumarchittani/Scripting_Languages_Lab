a = {}
while(True):
	print("Enter atomic element symbol or -1 ro exit")
	sym = input()
	if(sym=="-1"):
		break
	else:
		elem = input("Enter the name of element\n")
		a[sym]= elem
print("Adding unique element\n\n")
uniqueSym = input("Enter the symbol of unique element\n")
uniqueElem = input("Enter the element of unique element\n")
a[uniqueSym] = uniqueElem
print("Printing the dict after enetring unique element\n")
print(a)
print("Adding duplicate element")	
DupSym = input("Enter symbol of duplicate element")
DupElem	 = input("Enter the element name of duplicate element")
a[DupSym] = DupElem
print("Printing the dict after enetering duplicate element")
print(a)
print("No of elements in dictionary ",len(a))
search = input("Enter the element name to find")
for k,v in a.items():
	if v==search:
		print("Symbol for the element is",k)
		search = ""
if search!="":
	print("Element not present in dictionary")
				

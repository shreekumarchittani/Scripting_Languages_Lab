dict = {'na':'Sodium','H':'Hydrogen','he':'Helium'}
elemSym = input("Enter element Symbol ")
elemName = input("Enter element name ")
if elemSym not in dict:
    dict[elemSym] = elemName
print(dict)
print(len(dict))
elem = input("Enter the symbol of element to search   ")
if elem in dict:
    print("Element found is ",dict[elem])
else:
    print("Element not found")
def adding(list1,list2):
	return list1+list2
def reversing(lst):
	lst.reverse()
	return lst
#main program starts from here
print("Enter 2 lists")
''' map will assign the iterable to a function 
syntax : map(function,iterable)
input().split() will take the input as string
as space seperated'''
lst1 = list(map(int,input().split()))
lst2 = list(map(int,input().split()))	
print("Added original lists :",adding(lst1,lst2))
print("Reversed lists :")
print(reversing(lst1))
print(reversing(lst2))
print("Added reversed lists :",adding(lst1,lst2))	

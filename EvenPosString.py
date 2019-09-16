lst = list(map(str,input().split()))
for i in range(len(lst)):
	if i%2==0:
		print(lst[i],end=" ")
print()		
for i in range(2,len(lst),3):
	print(lst[i].upper())
lst.reverse()
print(lst)			

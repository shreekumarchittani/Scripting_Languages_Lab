lst = list(map(int,input().split()))
print('minimum: ',min(lst),'  maximum:  ',max(lst))
lst.append(int(input()))
print(lst)
lst.pop(2)
print("Enter the element to search")
x=int(input())
if x not in lst:
    print("Element not found")
else:
    print("Found")    
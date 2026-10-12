a=list(map(int, input("Enter number of elements:").split()))
item=int(input("Enter a number to be searched:"))
low=0
high=len(a)-1
found=False
while low<=high:
    mid=(low+high)//2
    if a[mid]==item:
        print("Element found",mid+1)
        found=True
        break
    elif a[mid]<item:
        low=mid+1
    else:
        high=mid-1

if found==False:
    print("Element not found")

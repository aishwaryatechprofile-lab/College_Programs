def linearSearch(theValues,target):
    for i in range(len(theValues)):
        if theValues[i]==target:
            return i
    return -1
theValues=list(map(int, input("Enter the elements:").split()))
target=int(input("Enter element to be searched:"))
position=linearSearch(theValues,target)
if position!=-1:
    print("Element found:",position)
else:
    print("Element not found")
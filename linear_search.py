def linearSearch(theValues,target):
    for i in range(len(theValues)):
        if theValues[i]==target:
            return i
    return -1
theValues=list(map(int,input("Enter elements:").split()))
target=int(input("Enter number to be searched:"))
position=linearSearch(theValues,target)
if position!=-1:
    print("Elemnt found at position: ",position)
else:
    print("Element not found")
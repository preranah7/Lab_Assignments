# Ternary search is a Divide and conquer algorithm
# divides array/list in three parts
# array provided should be sorted

arr = [1,2,3,4,5,6,7,8,9,10]
key = 4
start = 0
end = len(arr)-1

def Ternary_Search(arr,key,start,end):

    while(start<=end):
    #mid1 and mid2 are indices
        mid1 = start + (end - start)//3 #// floor operation to round off
        mid2 = end - (end - start)//3

        #comparisons
        if(arr[mid1]==key):
            return mid1
        if(arr[mid2]==key):
            return mid2
    
        #cases
        if(key < arr[mid1]):
            end = mid1 - 1
        elif(key > arr[mid2]):
            start = mid2 + 1
        elif(arr[mid1] < key and key < arr[mid2]):
            start = mid1 + 1
            end = mid2 - 1
    else:
        return -1
        
result = Ternary_Search(arr,key,start,end)
if(result != -1):
    print(f"Element {key} found at index {result}")
else:
    print(f"Element {key} not found in the array")

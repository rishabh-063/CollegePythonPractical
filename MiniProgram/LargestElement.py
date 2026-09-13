
#  write a program to find the largest element in the arrry

arr = [34,3,52,1,5,3,67,9,7]

arr.sort(reverse=True)

print(arr)
print(arr[0])

# Function to find the largest element in an array
def findLargestElement(arr):
    maxElement = arr[0]  
    for element in arr[1:]:
        if element > maxElement:
            maxElement = element  # update maxElement value if largest value found
    return maxElement

largestValue = findLargestElement(arr)
print(f"The largest element in the array is : {largestValue}")
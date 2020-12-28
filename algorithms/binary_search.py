#!/usr/bin/env python

 # ITERATIVE

def binary_search(the_list, x):
    """Binary search
    Precondition: List os ordered
    Return None if x is not in the list
    Return index suche the_list[index] == x
    """

    # Search in all the list, dividing in segments. Considering complete list as
    # segment that starts in 0 and finish in len(list)-1.

    izq = 0 # index of start of segment
    der = len(the_list) -1 # Index of end of segment

    # Segment is empty (or done searching) when index overlap
    while izq <= der:
        # Mid of segment
        medio = (izq+der)//2

        print("DEBUG:", "izq:", izq, "der:", der, "medio:", medio)

        if the_list[medio] == x:
            return medio

        # if value of middle is more than the value, continue searching but
        # using as segment, the one on the left [left, mid-1] , as we know that
        # it will be there. Right is discarded
        elif the_list[medio] > x:
            der = medio-1

        # same logic, but with other segment
        else:
            izq = medio+1

    # cycle finish, did not find value
    return None

# RECURSIVE


# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):

    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1

# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10

# Function call
result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

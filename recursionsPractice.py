import math

# find sum of an array/list. Diffculty: Easy
def sum(A):
    if not A:
        return 0
    if len(A)==1:
        return A[0]
    if len(A)>1:
        return A[0]+sum(A[1:])

# print(sum([1,2,3]))

# find Minimum of an array. Diffculty: Easy
def basicMin(A, currMin):
    if not A:
        return currMin
    if currMin>A[0]:
        currMin=A[0]
    return basicMin(A[1:],currMin)

# optimized version of finding min. Diffculty: Easy
def findMin(A, l, r):
    if l==r:
        return A[r]
    mid = math.floor((l+r)/2)
    leftMin = findMin(A,l , mid)
    rightMin = findMin(A, mid+1, r)
    return min(leftMin, rightMin)

# print( findMin([3,1,2]))

# checks if a string is a palindrom. Diffculty: medium
def isPali(text):
    if len(text)<= 1:
        return 1
    elif text[0] != text[len(text)-1]:
        return 0
    else:
        temp = text[1:-1]
        return isPali(temp)

# print(  isPali('ssws') )

# reverse a list recursivly. Diffculty: Medium.
def reverseList(A,rev):
    if not A:
        return
    reverseList(A[1:],rev)
    rev.append(A[0])

# rev = []
# reverseList([3,2,1],rev)
# print(rev)

# find a subsets of a set. Diffculty: Hard
def print_set(subset):
    temp = []
    for x in subset:
        if x!= None:
            temp.append(x)
    print(temp)

def all_subsets(given_array):
    subset = [None] * len(given_array)
    helper(given_array,subset,0)

def helper(given_array, subset, i):
    if i==len(given_array):
        print_set(subset)
    else:
        subset[i] = None
        helper(given_array,subset,i+1)
        subset[i] = given_array[i]
        helper(given_array,subset,i+1)

all_subsets([1,2])


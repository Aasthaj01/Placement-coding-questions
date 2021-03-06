#Given an integer array and a positive integer k, count all distinct pairs with difference equal to k.


# O(n^2) solution
def pair_with_diff_k(arr, minDiff):
    count = 0
    for i in range(0, len(arr)):
        for j in range(1+i, len(arr)):
            if arr[i]-arr[j] == minDiff or arr[j]-arr[i] == minDiff:
                count = count+1
            else:
                continue
    return count 
  
  
arr = list(map(int, input("Enter the elements of arr:").split()))
k = int(input("Enter the difference:"))
ans = pair_with_diff_k(arr, k)
print("The number of distinct pairs with difference as k are:", ans)  
#=================================================================================================================
# O(nlogn) solution
def pair_with_diff_k(arr, k): 
    n = len(arr)
    count =0
    arr.sort()  
    l =0
    r=0
    while r<n: 
        if arr[r]-arr[l]==k: 
            count+=1
            l+=1
            r+=1
        elif arr[r]-arr[l]>k:  
            l+=1
        else: 
            r+=1
    return count 
    
    
arr = list(map(int, input("Enter the elements of arr:").split()))
k = int(input("Enter the difference:"))
ans = pair_with_diff_k(arr, k)
print("The number of distinct pairs with difference as k are:", ans)  
#==================================================================================================================

def pair(arr, k):
    sett = set(arr)
    count = 0
    for num in sett:
        if(num+k in sett):
            count += 1
    return count
    
arr = list(map(int, input("Enter the elements of arr:").split()))
k = int(input("Enter the difference:"))
ans = pair(arr, k)
print("The number of distinct pairs with difference as k are:", ans) 
#===================================================================================================================

from collections import Counter

def pair(arr, k):
    counter = Counter(arr)
    
    count = 0
    for i in arr:
        find = i-k
        if(find in counter):
            count+=1
        
    return count
arr = [ 1, 2, 4, 8, 8, 12 ] 
k = 3

n = len(arr) 
ans = pair(arr, k)   
print(ans)
    

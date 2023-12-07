'''
First Loop (i): range(n - 2)
We use range(n - 2) to ensure that there is enough room for j and k after i. If i is at index n - 2 or beyond, there won't be enough elements left for j and k.

Second Loop (j): range(i + 1, n - 1)
We use range(i + 1, n - 1) to ensure that j is always greater than i. This avoids checking the same pair of indices in reverse order and ensures a strictly increasing sequence.

Third Loop (k): range(j + 1, n)
We use range(j + 1, n) to ensure that k is always greater than j. Similar to the second loop, this ensures that we are considering unique indices for j and k in a strictly increasing sequence.

'''
def increasing_triplet_subsequence_bruteforce(arr):
    result=False
    for i in range(len(arr)-2):
        for j in range(i+1,len(arr)-1):
            for k in range(j+1,len(arr)):
                if arr[i]<arr[j]<arr[k]:
                    result=True
    return result



'''
The key idea here is to maintain two variables (small and second_small) to track the two smallest elements encountered so far.
If we find a number greater than both small and second_small, we have found an increasing triplet.
By updating small and second_small as we iterate through the array, we ensure that we are looking for a larger number each time, satisfying the condition for an increasing triplet.


'''
def increasing_triplet_subsequence_optimized(arr):
    small,second_small=float('inf'),float('inf')

    for i in arr:
        if i<=small:
            small=i
        elif i<=second_small:
            second_small=i 
        else:
            return True
    return False

if __name__=="__main__":
    print(increasing_triplet_subsequence_bruteforce([2,1,5,0,4,6]))
    print(increasing_triplet_subsequence_optimized([2,1,5,0,4,6])) 
            
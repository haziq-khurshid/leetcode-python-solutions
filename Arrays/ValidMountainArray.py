class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        n = len(arr)
        if n < 3: return False                          # Array length should be greater or equal to 3 to be a valid mountain
        i, j = 0, n-1                                   # Initializing pointers at start and end of array
        while i+1 < n and arr[i] < arr[i+1]:            # While first pointer doesn't reach end of the array and numbers are in increasing order
            i+=1                                        # Keep taking pointer forward
        while j > 0 and arr[j] < arr[j-1]:              # While last pointer doesn't reach start of the array and numbers are in decreasing order
            j-=1                                        # Keep bringing pointer backwards

        return i == j and i > 0 and j < n -1            # If both pointers are at same spot and it's neither start or end of array
                                                        # it is a valid mountan array


"""Below is the function call to test above function,
    you can change arr in input"""
def main():
    arr = [0,3,2,1]
    sol = Solution()
    result = sol.validMountainArray(arr)
    print(result)

if __name__ == "__main__":
    main()
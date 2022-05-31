class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i = m - 1           # pointer for last number in nums1
        j = n - 1           # pointer for last number in nums2
        k = m + n -1        # pointer for last index in nums1
        
        """ Sorting is done in reverse order """
        while j >= 0:
            if i >=0 and nums1[i] > nums2[j]:           # If last number of nums1 is greater than last number of nums2
                nums1[k] = nums1[i]                     # Place last number of nums1 at the position of index pointer
                k-=1                                    # Bring index pointer a step back
                i-=1                                    # Bring nums1 number pointer a step back
            else:
                nums1[k] = nums2[j]                     # Else place last number of nums2 at the position of index pointer
                k-=1                                    # Bring index pointer a step back
                j-=1                                    # Bring nums2 number pointer a step back
        

"""Below is the function call to test above function,
    you can changes nums & their length in input"""
def main():
    nums1 = [1,5,8,0,0,0]             
    nums2 = [2,4,9]
    m = 3           #length of actual numbers in nums1
    n = 3           #length of nums2
    sol = Solution()
    sol.merge(nums1,m,nums2,n)
    
if __name__ == "__main__":
    main()
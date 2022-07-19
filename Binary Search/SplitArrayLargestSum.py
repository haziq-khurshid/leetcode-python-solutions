class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        lb = max(nums)                          # Taking maximum number as lower bound
        ub = sum(nums)                          # Taking sum of numbers as upper bound
                                                # Solution lies in lb & ub, so applying binary search there
        while lb < ub:
            mid = lb + ((ub-lb)//2)
            tmp_sum = 0                         # Temp sum to track sum of numbers in a partition
            arr_count = 1                       # Array count to keep track of partitions
            for num in nums:
                if tmp_sum + num <= mid:        # If sum in a partition plus current number is in bound of mid value
                    tmp_sum += num              # Add number in the partition
                else:
                    arr_count += 1              # Else increase the count
                    tmp_sum = num               # and set tmo_sum to current number
            if arr_count > m:                   # If partitions exceeds size in input
                lb = mid + 1                    # Bring lower bound ahead of mid as answer lies between mid & upper bound
            else:
                ub = mid                        # Else bring upper bound to mid as answer lies between lower bound & mid
        return ub
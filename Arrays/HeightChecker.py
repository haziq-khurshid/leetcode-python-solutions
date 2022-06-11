class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        count = 0                                   # Keep track of out of position heights
        expected = sorted(heights)                  # Creating new array with correct positioning
        for i in range(len(heights)):               
            if heights[i] != expected[i]:           # Compare if expected vs actual height matches at any position
                count+=1                            # Increase count if true
        return count

"""Below is the function call to test above function,
    you can change heights in input"""
def main():
    heights = [5,1,2,3,4]
    sol = Solution()
    count = sol.heightChecker(heights)
    print(count)

if __name__ == "__main__":
    main()
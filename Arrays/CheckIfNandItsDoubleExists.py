from operator import truediv
from unittest import result


class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        visited = set()                                   # Create an empty set to track visited numbers
        for num in arr:
            if num*2 in visited or num/2 in visited:      # Check if double or half of number exists in the visited set
                return True
            else:
                visited.add(num)
        return False


"""Below is the function call to test above function,
    you can change arr in input"""
def main():
    arr = [3,1,7,11]
    sol = Solution()
    result = sol.checkIfExist(arr)
    print(result)

if __name__ == "__main__":
    main()
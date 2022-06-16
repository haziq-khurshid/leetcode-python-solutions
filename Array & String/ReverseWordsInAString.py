class Solution:
    def reverseWords(self, s: str) -> str:
        res = " ".join(s.split()[::-1])         # Using split function to split string into a list based upon spaces
                                                # Join the list after reversing the order
        return res

"""Below is the function call to test above function,
    you can change string in the input"""
def main():
    s = "hello world"
    sol = Solution()
    rev_string = sol.reverseWords(s)
    print(rev_string)

if __name__ == "__main__":
    main()
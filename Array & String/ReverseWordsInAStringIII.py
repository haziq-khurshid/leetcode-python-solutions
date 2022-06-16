class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(word[::-1] for word in s.split())       # For each word in string, reverse the word
                                                                # and then join and return the answer

"""Below is the function call to test above function,
    you can change string in the input"""
def main():
    s = "hello world"
    sol = Solution()
    rev_string = sol.reverseWords(s)
    print(rev_string)

if __name__ == "__main__":
    main()
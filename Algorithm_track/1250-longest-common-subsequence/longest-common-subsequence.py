class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memoization = {}
        def dp(i, j):
            # base case
            if i >= len(text1) or j >= len(text2):
                return 0
            if (i, j) not in memoization:
                if text1[i] == text2[j]: # you have got your subsequece element--update your count
                    memoization[(i, j)] = 1 + dp(i + 1, j + 1)
                else:
                    memoization[(i, j)] = max(dp(i, j + 1), dp(i + 1, j))

            return memoization[(i, j)]

        return dp(0, 0)
# LeetCode: Best Time to Buy and Sell Stock(easy)
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Input: [7,1,5,3,6,4]
# Output: 5





from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([7,1,5,3,6,4]))  # Expected output: 5

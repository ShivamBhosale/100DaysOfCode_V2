"""
# Coin Change Problem
<hr>

Note: This problem has multiple solutions and is a classic problem in showing issues with basic recursion. There are better solutions involving memoization and simple iterative solutions.If you are having trouble with this problem (or it seems to be taking a long time to run in some cases) check out the Solution Notebook and fully read the conclusion link for a detailed description of the various ways to solve this problem!

This problem is common enough that is actually has its own Wikipedia Entry! Let's check the problem statement again:

This is a classic recursion problem: Given a target amount n and a list (array) of distinct coin values, what's the fewest coins needed to make the change amount.

For example:

If n = 10 and coins = [1,5,10]. Then there are 4 possible ways to make change:

   <li> 1+1+1+1+1+1+1+1+1+1

   <li> 5 + 1+1+1+1+1

   <li> 5+5
   <li> 10

With 1 coin being the minimum amount.
## Solution

This is a classic problem to show the value of dynamic programming. We'll show a basic recursive example and show why it's actually not the best way to solve this problem.

Make sure to read the comments in the code below to fully understand the basic logic!
"""

def rec_coin(target,coins):
    min_coins = target

    if target in coins:
        return 1
    else:
        for i in [c for c in coins if c <= target]:
            num_coins = 1 + rec_coin(target-i,coins)

            if num_coins < min_coins:
                min_coins = num_coins
    return min_coins

print(rec_coin(10,[1,5,10,2]))
print(rec_coin(63,[1,5,10,25]))
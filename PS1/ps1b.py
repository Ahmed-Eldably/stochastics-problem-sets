###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

# ================================
# Part B: Golden Eggs
# ================================

# Problem 1
from hashlib import new
from time import time
from unittest import result


def dp_make_weight_without_memoization(egg_weights, target_weight):
    # if there are no eggs to consider
    if len(egg_weights) == 0:
        return 0
    # if the heaviest egg would exceed the maximum capacity
    elif (target_weight - egg_weights[-1]) < 0:
        return dp_make_weight_without_memoization(egg_weights=egg_weights[:-1], target_weight=target_weight)
    # if we successfully filled up the ship with capacity we want.
    elif target_weight - egg_weights[-1] == 0:
        return 1
    else:
        # egg weights stay the same but the new target weight
        # becomes the difference between the old target weight and the heaviest egg
        lhs = 1 + dp_make_weight_without_memoization(egg_weights=egg_weights, target_weight=target_weight - egg_weights[-1])
        rhs = dp_make_weight_without_memoization(egg_weights=egg_weights[:-1], target_weight=target_weight)

    if lhs > 0 and rhs > 0:
        return min(lhs, rhs)
    else:
        return max(lhs, rhs)


def dp_make_weight(egg_weights, target_weight, memo={}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.

    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)

    Returns: int, the smallest number of eggs needed to make target weight
    """
    # TODO: Your code here

    # if the tuple key (egg_weights, target_weight) in the dict memo
    if (egg_weights, target_weight) in memo:
        return memo[(egg_weights, target_weight)]
    else:
        # if there are no eggs to consider
        if len(egg_weights) == 0:
            memo[(egg_weights, target_weight)] = 0
            return 0
        # if the heaviest egg would exceed the maximum capacity
        elif (target_weight - egg_weights[-1]) < 0:
            return dp_make_weight(egg_weights=egg_weights[:-1], target_weight=target_weight)
        # if we successfully filled up the ship with capacity we want.
        elif target_weight - egg_weights[-1] == 0:
            memo[(egg_weights, target_weight)] = 1
            return 1
        else:
            # egg weights stay the same but the new target weight
            # becomes the difference between the old target weight and the heaviest egg
            lhs = 1 + dp_make_weight(egg_weights=egg_weights, target_weight=target_weight - egg_weights[-1])
            rhs = dp_make_weight(egg_weights=egg_weights[:-1], target_weight=target_weight)

        if lhs <= 0 or rhs <= 0:
            memo[(egg_weights, target_weight)] = max(lhs, rhs)
            return max(lhs, rhs)
        else:
            memo[(egg_weights, target_weight)] = min(lhs, rhs)
            return min(lhs, rhs)


# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 15, 20, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print(f"n = {n}")
    start = time()
    # print("Expected output: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    end = time()
    print("Total time with memoization took %f seconds" % (end - start))
    start = time()
    print()
    print("Actual output:", dp_make_weight_without_memoization(egg_weights, n))
    end = time()
    print("Total time without memoization took %f seconds" % (end - start))
    print()

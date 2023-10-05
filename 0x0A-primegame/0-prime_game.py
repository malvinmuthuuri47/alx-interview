#!/usr/bin/python3
"""Prime Game"""
from collections import defaultdict


def isWinner(x, nums):
    """Find winner"""
    def is_prime(num):
        """Check that number is prime"""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def calculate_winner(n):
        """Calculate winner function"""
        m = defaultdict(int)
        for i in range(2, n + 1):
            if is_prime(i):
                for j in range(i, n + 1, i):
                    m[j] += 1

        maria_turn = True
        while True:
            can_choose_prime = False
            for num in m:
                if m[num] > 0:
                    can_choose_prime = True
                    m[num] -= 1
                    break

            if not can_choose_prime:
                return "Ben" if maria_turn else "Maria"

            maria_turn = not maria_turn

    winners = []
    for n in nums:
        winner = calculate_winner(n)
        winners.append(winner)

    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """A function that determines the winner of the prime game"""
    def is_prime(num):
        """A function that determines if the array has numbers greater
        than 2 that fit to be prime numbers"""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Create a list to store the winners for each round
    winners = []

    # Iterate through each round
    for n in nums:
        # Calculate the total count of prime numbers in the range [1, n]
        prime_count = sum(1 for i in range(2, n + 1) if is_prime(i))

        # Determine the winner based on the parity of the prime count
        # If the count is even, Ben wins; otherwise, Maria wins
        if prime_count % 2 == 0:
            winners.append("Ben")
        else:
            winners.append("Maria")
    # Count the number of times each player wins
    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

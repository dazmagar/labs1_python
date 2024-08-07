"""
To try and encourage more sales of different books from a popular 5-book series, a bookshop has decided to offer discounts on multiple book purchases. 
One copy of any of the five books costs $8. 
If, however, you buy two different books, you get a 5% discount on those two books. 
If you buy 3 different books, you get a 10% discount. 
If you buy 4 different books, you get a 20% discount. 
If you buy all 5, you get a 25% discount. 
Note that if you buy four books, of which 3 are different titles, you get a 10% discount on the 3 that form part of a set, but the fourth book still costs $8. 
"""

from collections import Counter
from operator import mul

DISCOUNT_PRICE = [0, 800, 1520, 2160, 2560, 3000]
price = {i + 1: 800 * (i + 1) * p for i, p in enumerate([1, 0.95, 0.9, 0.8, 0.75])}
PRICES = (800, 1520, 2160, 2560, 3000)


def total1(basket):
    price = len(basket) * 800
    counter = Counter(basket)

    for i in range(1, len(counter) + 1):
        remain = counter - Counter(k for k, _ in counter.most_common(i))
        price = min(price, DISCOUNT_PRICE[i] + total1(list(remain.elements())))

    return price


def total2(basket):
    def rec(counts, mgs):
        if not (g := counts.most_common(mgs)):
            return 0
        counts = counts - Counter(a for a, _ in g)
        return price[len(g)] + min(rec(counts, mgs) for mgs in range(len(g)))

    return min(rec(Counter(basket), mgs) for mgs in range(len(price)))


def total3(basket: list[int]) -> int:
    counts = sorted((basket.count(x) for x in set(basket)), reverse=True) + [0] * 5
    groups = [x - counts[i] for i, x in enumerate(counts[:-1])]
    while groups[2] and groups[4]:
        groups[4] -= 1
        groups[2] -= 1
        groups[3] += 2
    return sum(mul(*x) for x in zip(PRICES, groups))


def total4(basket):
    books = sorted(Counter(basket).values(), reverse=True)
    if 4 < len(books):
        books.append(min(books[2] - books[3], books[4]))

    costs = [800, 720, 640, 480, 440, -40]
    return sum(amt * cost for amt, cost in zip(books, costs))


# Example usage
basket = [1, 1, 2, 2, 3, 3]
print(total1(basket))  # Expected output: 5120 cents (or $51.20)

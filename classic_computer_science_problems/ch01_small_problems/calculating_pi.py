# calculating_pi.py
"""
Calculate pi using the Leibniz formula
pi = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 ...
"""
from rich import print


def calculate_pi(n_terms: int) -> float:
    """
    Larger the value of `n_terms`, more accurate the sum is to pi.
    """
    p: float = 4.0
    q: float = 1.0
    op: float = 1.0
    pi: float = 0.0
    
    for _ in range(n_terms):
        pi += op * (p / q)
        q += 2.0
        op *= -1.0
    
    return pi


if __name__ == '__main__':
    n = 100_000
    print(f'Sum of Leibniz series with {n:,} terms: {calculate_pi(n)}')
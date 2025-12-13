# ladder.py

def my_steps(n):
    if not isinstance(n, int) or n < 1 or n > 25:
        raise ValueError("n must be an integer between 1 and 25")

    # base cases
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    # ways(1), ways(2), ways(3)
    a, b, c = 1, 2, 4

    # compute ways(4) up to ways(n)
    for _ in range(4, n + 1):
        a, b, c = b, c, a + b + c

    return c

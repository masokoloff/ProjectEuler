def is_prime(val):
    if int(val) != val or val < 0:
        raise ValueError
    if val < 2:
        return False
    for i in range(2, int(val ** 0.5) + 1):
        if not val % i:
            return False
    return True

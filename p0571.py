import itertools


def numberToBase(n, b):
    if b > 16:
        raise ValueError
    symbols = '0123456789ABCDEF'
    if n == 0:
        return '0'
    digits = []
    while n:
        digits.append(symbols[int(n % b)])
        n //= b
    return ''.join(digits[::-1])


def is_b_pandigital(n, b):
    if b > 16:
        raise ValueError
    symbols = '0123456789ABCDEF'
    base_symbols_set = set(symbols[:b])
    if not base_symbols_set.difference(n):
        return True
    return False


p_gen = itertools.permutations('0123456789AB')
s_pandig = []
for p in p_gen:
    if p[0] == '0':
        continue
    s = ''.join(p)
    d = int(s, 12)
    is_super_pandigital = True
    for b in range(2, 13)[::-1]:
        if not is_b_pandigital(numberToBase(d, b), b):
            is_super_pandigital = False
            break
    if is_super_pandigital:
        s_pandig.append(d)
        print(len(s_pandig))
    if len(s_pandig) == 10:
        print(sum(s_pandig))
        break
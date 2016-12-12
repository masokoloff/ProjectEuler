from lib import is_prime


def repeating_digits(val):

    if len(set(str(val))) == len(str(val)):
        return []
    result = []
    for d in set(str(val)):
        if str(val).count(d) > 1:
            result.append(int(d))
    return result

i = 1
done = False
while True:
    if done:
        break
    i += 1
    if is_prime(i) and repeating_digits(i):
        for digit in repeating_digits(i):
            bad = 0
            prostye = [i]
            for j in range(10):
                if digit == j:
                    continue
                new_i = int(str(i).replace(str(digit), str(j)))
                if len(str(new_i)) != len(str(i)) or not is_prime(new_i):
                    bad += 1
                else:
                    prostye.append(new_i)
                if bad > 2:
                    break
            if bad <= 2:
                print(i)
                done = True

def countSumOfTwoRepresentations(n, l, r):
    result = 0

    for a in range(l, r+1):
        b = a
        while b <= r:
            if a + b == n:
                result += 1
            b += 1

    return result

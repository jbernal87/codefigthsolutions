def almostIncreasingSequence(s):  
    droppped = False
    last = prev = min(s) - 1
    for elm in s:
        if elm <= last:
            if droppped:
                return False
            else:
                droppped = True
            if elm <= prev:
                prev = last
            elif elm >= prev:
                prev = last = elm
        else:
            prev, last = last, elm
    return True

from itertools import takewhile
matrixElementsSum = lambda m: sum([sum(takewhile(lambda x: x>0, row)) for row in list(zip(*m))])

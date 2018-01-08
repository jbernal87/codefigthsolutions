adjacentElementsProduct = lambda a: max([a[i] * a[i+1] for i, _ in enumerate(a[:-1])])

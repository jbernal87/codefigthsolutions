def makeArrayConsecutive2(s):
       return len(list(filter( lambda x: x not in s, range(min(s),max(s)) )))

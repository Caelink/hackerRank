def isValid(l1, l2, l3):
    return (l1 + l2 > l3) and (l1 + l3 > l2) and (l3 + l2 > l1)

def findBiggestTriangle(lst):
    for n, j in enumerate(lst):
        for m, k in enumerate(lst[n+1:], start=n+1):
            for l in lst[m+1:]:
                if isValid(j,k,l):
                    return [j, k, l]
    return []

n = int(raw_input())
lst = map(int, raw_input().split(' '))
lst = sorted(lst, reverse=True)

biggestTriangle = findBiggestTriangle(lst)
if biggestTriangle:
    print'%d %d %d'%(biggestTriangle[2], biggestTriangle[1], biggestTriangle[0])
else:
    print '-1'

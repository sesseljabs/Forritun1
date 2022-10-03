from copy import deepcopy
amg = [[0]*3]*2
umg = amg[:]
e = deepcopy(umg)
amg[0][0] = 1
amg[0].pop()
amg[0].pop()
print(amg)
print(umg)
print(e)
from random import getrandbits

RANDOM = getrandbits(32)

class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)
    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM

print([hash(x) for x in range(5)])
print([hash(Wrapper(x)) for x in range(5)])
print(hash(Wrapper(1)), hash(Wrapper(1+(1<<32))))
print([hash(str(x)) for x in range(5)])


d = {}
for i in range(5):
  d[Wrapper(i)] = i
print(d)
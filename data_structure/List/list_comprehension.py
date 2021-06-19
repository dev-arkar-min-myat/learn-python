# List Comprehension

>>> squares = []
>>> for x in range(10):
...     squares.append(x**2)
... 
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> squares = list(map(lambda x:x**2,range(10)))
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> squares = [x**2 for x in range(10)]
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

>>> combs = []
>>> for x in [1,2,3]:
...     for y in [3,1,2]:
...             if x != y:
...                     combs.append((x,y))
... 
>>> combs
[(1, 3), (1, 2), (2, 3), (2, 1), (3, 1), (3, 2)]
>>> vec = [-4,-2,0,2,4]
>>> [x**2 for x in vec]
[16, 4, 0, 4, 16]
>>> [x for x in vec if x > 0]
[2, 4]
>>> [abs(x) for x in vec]
[4, 2, 0, 2, 4]
>>> [(x,x**2) for x in range(6)]
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
>>> from math import pi
>>> [str(round(pi,i)) for i in range(1,6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']



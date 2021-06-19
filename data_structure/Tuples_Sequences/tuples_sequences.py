# Tuple and Sequences

>>> t = 12345,54321,'hello'
>>> t
(12345, 54321, 'hello')
>>> t[0]
12345
>>> type(t)
<class 'tuple'>
>>> u = t,(1,2,3,4,5)
>>> u
((12345, 54321, 'hello'), (1, 2, 3, 4, 5))
>>> v = ([1,2,3],[3,2,1])
>>> v
([1, 2, 3], [3, 2, 1])
>>> empty = ()
>>> len(empty)
0
>>> singleton = 'hello'
>>> len(singleton)
5
>>> singleton
'hello'

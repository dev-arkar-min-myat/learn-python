# Nested List Comprehension

>>> matrix = [
... [1,2,3,4],
... [5,6,7,8],
... [9,10,11,12],
... [13,14,15,16]
... ]
>>> 
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]]
>>> transposed = []
>>> for i in range(4):
...     transposed.append([row[i] for row in matrix])
... 
>>> transposed
[[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]

>>> list(zip(*matrix))
[(1, 5, 9, 13), (2, 6, 10, 14), (3, 7, 11, 15), (4, 8, 12, 16)]
>>> 
]

# List as Queues

>>> from collections import deque
>>> queue = deque(["apple","orange","grape"])
>>> queue
deque(['apple', 'orange', 'grape'])
>>> queue.append("banana")
>>> queue
deque(['apple', 'orange', 'grape', 'banana'])
>>> queue.append("kiwi")
>>> queue
deque(['apple', 'orange', 'grape', 'banana', 'kiwi'])
>>> queue.popleft()
'apple'
>>> queue
deque(['orange', 'grape', 'banana', 'kiwi'])
>>> queue.popleft()
'orange'
>>> queue
deque(['grape', 'banana', 'kiwi'])

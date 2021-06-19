# Set

>>> baskets = {'apple','orange','grape','banana','grape','apple'}
>>> baskets
{'orange', 'grape', 'apple', 'banana'}
>>> 'orange' in baskets
True
>>> 'kiwi' in baskets
False
>>> a = set('abracadabra')
>>> a
{'r', 'a', 'c', 'd', 'b'}
>>> b = set('alacazam')
>>> b
{'l', 'a', 'c', 'm', 'z'}
>>> a-b			# letter in a but not b
{'r', 'd', 'b'}
>>> a | b  		# letters in a or b or both
{'l', 'r', 'a', 'c', 'm', 'z', 'd', 'b'}
>>> a & b  		# letters in both a and b
{'c', 'a'}
>>> a ^ b  		# letters in a not but in b
{'l', 'm', 'z', 'd', 'b', 'r'}
>>> a = {x for x in 'abracadabra' if x not in 'abc'} 
>>> a
{'r', 'd'}

# Looping Technique

>>> hero = {'rubick':'intel','axe':'stren','drow ranger':'agil'}
>>> for k,v in hero.items():
...     print(k,v)
... 
rubick intel
axe stren
drow ranger agil
>>> for i,v in enumerate(['tic','tac','toe']):
...     print(i,v)
... 
0 tic
1 tac
2 toe
>>> hero = ['rubick','axe','luna']
>>> attr = ['intel','stren','agil']
>>> for h,a in zip(hero,attr):
...     print('hero {0},{1}'.format(h,a))
... 
hero rubick,intel
hero axe,stren
hero luna,agil
>>> for i in reversed(range(1,10,2)):
...     print(i)
... 
9
7
5
3
1
>>> basket = ['apple','orange','banana','kiwi','orange','apple','banana']
>>> basket
['apple', 'orange', 'banana', 'kiwi', 'orange', 'apple', 'banana']
>>> for i in sorted(basket):
...     print(i)
... 
apple
apple
banana
banana
kiwi
orange
orange
>>> for i in sorted(set(basket)):
...     print(i)
... 
apple
banana
kiwi
orange
>>> import math
>>> raw_data = [56.2,float('NaN'),51.7,55.3,52.5,float('NaN'),47.8]
>>> raw_data
[56.2, nan, 51.7, 55.3, 52.5, nan, 47.8]
>>> filtered_data = []
>>> for value in raw_data:
...     if not math.isnan(value):
...             filtered_data.append(value)
... 
>>> filtered_data
[56.2, 51.7, 55.3, 52.5, 47.8]

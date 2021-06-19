# Dictionary

>>> tel = {'tel':2034,'snape':3465}
>>> tel
{'tel': 2034, 'snape': 3465}
>>> tel['guido'] = 4567
>>> tel
{'tel': 2034, 'snape': 3465, 'guido': 4567}
>>> tel['snape']
3465
>>> del tel['guido']
>>> tel
{'tel': 2034, 'snape': 3465}
>>> tel['irvl'] = 1467
>>> tel
{'tel': 2034, 'snape': 3465, 'irvl': 1467}
>>> list(tel)
['tel', 'snape', 'irvl']
>>> sorted(tel)
['irvl', 'snape', 'tel']
>>> 'guido' in tel
False
>>> 'snape' in tel
True
>>> dict([('amber',1234),('storm',4567),('void',8900)])
{'amber': 1234, 'storm': 4567, 'void': 8900}
>>> {x:x**2 for x in (2,4,6)}
{2: 4, 4: 16, 6: 36}

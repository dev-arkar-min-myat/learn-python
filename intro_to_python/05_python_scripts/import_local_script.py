# import local script

import list_useful_function
import other_script
print(other_script.num)

scores = [23,45,56,24,87,90]

mean = list_useful_function.mean(scores)
curved = list_useful_function.add_five(scores)
m_curved = list_useful_function.mean(curved)

print(scores)
print(mean)
print(curved)
print(m_curved)


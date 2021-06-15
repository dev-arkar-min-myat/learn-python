# List and Membership Operator

# List is a mutable ordered sequence for elements.

# define list
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
print(months[0])
print(months[1])
print(months[2])
print(months[-1])

# Slice and dice List

q3 = months[7:9]
print(q3)

print(months[:6])
print(months[6:])

print(len(months))

print('May' in months)
print('Sun' in months)

# Mutablity-whether an object can change its values after it has been created

my_list = [1,2,3.4,"String",'Character']
print(my_list)

my_list[0] = "list"
print(my_list)

num_list = [2,3,5,1,3,7,9,100,4,5]

print(len(num_list))

print(max(num_list))

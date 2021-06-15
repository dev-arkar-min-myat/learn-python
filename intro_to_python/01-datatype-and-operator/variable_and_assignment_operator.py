# Variable and Assignment Operator

mv_population = 74728
# my_population => variable name
# = => assignment operator
# 74728 => value
print(mv_population)

# From right to left (value to variable)
x = 2
y = x
print(y)
print(x)

# declare multiple variables
x,y,z = 2,3,4
print(x,y,z)

# reduce duplication of variable with assignment operator
mv_population += 4000-600
print(mv_population)

# Quiz
# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff
rainfall -= rainfall * 0.1
print(rainfall)

# add the rainfall variable to the reservoir_volume variable
reservoir_volume += rainfall
print(reservoir_volume)

# increase reservoir_volume by 5% to account for stormwater that flows
reservoir_volume += reservoir_volume * 0.05
print(reservoir_volume)

# into the reservoir in the days following the storm
# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume -= reservoir_volume * 0.05
print(reservoir_volume)

# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
# print the new value of the reservoir_volume variable

reservoir_volume -= 2.5e5
print(reservoir_volume)

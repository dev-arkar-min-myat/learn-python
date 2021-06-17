# Define Function

def cylinder_volume(height,radius):
    pi = 3.142
    return height * pi * radius ** 2

print(cylinder_volume(18,3))

def printHello():
    print("Hello World")

printHello()

# default argument

def cylinder_volume_with_argument(height,radius = 5):
    pi = 3.142
    return height * pi * radius ** 2

print(cylinder_volume_with_argument(10))
print(cylinder_volume_with_argument(10,10))

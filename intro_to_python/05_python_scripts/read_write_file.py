# Read and Write Files

f = open('demo.txt','r')

file_data = f.read()
print(file_data)

f.close()

# Write File

file = []
for i in range(1000):
    file.append(open('demo.txt','r'))
    print(i)

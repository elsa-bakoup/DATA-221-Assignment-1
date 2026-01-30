from random import random

values = [random() for i in range(20)]
x = random()
values.sort()

index_track = -1          #keeping track of the index
index_count = []          #creating a list with all the matching indexes
for value in values:
    index_track += 1
    if value >= x:
        index_count.append(index_track)

print(values)
print(x)
if index_count:
    print(index_count[0])
else:
    print("No value greater than or equal to x")
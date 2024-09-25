import math

ListOfCoordinates = [(3,3), (3,5), (5,3), (1,2), (6,1), (8,2), (7,4), (4,6), (3,7), (2,8), (6,9)]
data = []
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

for i in range(1, len(ListOfCoordinates)):
    # you can use print or return, depending on your needs
    print(f"Distance of {ListOfCoordinates[i]} is {distance(ListOfCoordinates[0], ListOfCoordinates[i])}")
    data.append(distance(ListOfCoordinates[0], ListOfCoordinates[i]))
    
print(min(data))
print(max(data))
result = dict((i, data.count(i)) for i in data)
print(result)
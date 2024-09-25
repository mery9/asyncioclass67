import math
import asyncio

ListOfCoordinates = [(3, 3), (3, 5), (5, 3), (1, 2), (6, 1), (8, 2), (7, 4), (4, 6), (3, 7), (2, 8), (6, 9)]
data = []

async def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

async def calculate_distances():
    tasks = []
    for i in range(1, len(ListOfCoordinates)):
        task = asyncio.create_task(distance(ListOfCoordinates[0], ListOfCoordinates[i]))
        tasks.append(task)
    
    distances = await asyncio.gather(*tasks)
    for i, dist in enumerate(distances, 1):
        print(f"Distance of {ListOfCoordinates[i]} is {dist}")
        data.append(dist)

async def main():
    await calculate_distances()
    
    min_data = min(data)
    max_data = max(data)
    result = {i: data.count(i) for i in data}
    
    print(f"Min distance: {min_data}")
    print(f"Max distance: {max_data}")
    print(result)

# Running the async main function
asyncio.run(main())

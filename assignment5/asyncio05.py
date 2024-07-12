from random import random
import asyncio

async def cook_fried_rice():
    cooking_time = 1 + random()
    print(f">Fried rice cooked in {cooking_time}")
    await asyncio.sleep(cooking_time)
    return "Fried rice", cooking_time

async def cook_noodle():
    cooking_time = 1 + random()
    print(f">Noodle cooked in {cooking_time}")
    await asyncio.sleep(cooking_time)
    return "Noodle", cooking_time

async def cook_curry():
    cooking_time = 1 + random()
    print(f">Curry cooked in {cooking_time}")
    await asyncio.sleep(cooking_time)
    return "Curry", cooking_time

async def main():
    tasks = [
        asyncio.create_task(cook_fried_rice()),
        asyncio.create_task(cook_noodle()),
        asyncio.create_task(cook_curry())
    ]
   
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    
    print(f"Completed tasks: {len(done)}")
    print(f"Uncompleted tasks: {len(pending)}")

    first_completed_task = done.pop()
    first_dish, cooking_time = first_completed_task.result()
    print(f"First dish to complete is {first_dish} and finished in {cooking_time}")
    
    # await asyncio.gather(*done)
    # await asyncio.gather(*pending)
    print("All dishes are ready")

asyncio.run(main())
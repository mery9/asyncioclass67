from random import random
import asyncio

async def cook_fried_rice():
    cooking_time = 1 + random()
    await asyncio.sleep(cooking_time)
    print(f">Fried rice cooked in {cooking_time} minutes")
    return "Rice"

async def cook_noodle():
    cooking_time = 1 + random()
    await asyncio.sleep(cooking_time)
    print(f">Noodle cooked in {cooking_time} minutes")
    return "Noodle"

async def cook_curry():
    cooking_time = 1 + random()
    await asyncio.sleep(cooking_time)
    print(f">Curry cooked in {cooking_time} minutes")
    return "Curry"

async def main():
    tasks = [
        asyncio.create_task(cook_fried_rice()),
        asyncio.create_task(cook_noodle()),
        asyncio.create_task(cook_curry())
    ]
    
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    
    first_dish = done.pop().result()
    print(f"Student A can eat the {first_dish} first")

    await asyncio.gather(*pending)
    print("All dishes are ready")

asyncio.run(main())
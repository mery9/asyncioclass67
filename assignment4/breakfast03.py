# Asynchronous breakfast
import asyncio
from time import sleep, time

async def make_coffee():  # 1
    print("coffee: prepare ingridients")
    print("coffee: waiting...")
    await asyncio.sleep(5)  # 2: pause, another tasks can be run
    print("coffee: ready")

async def fry_eggs():  # 1
    sleep(1) # pause, for 1 sec
    print("eggs: prepare ingridients")
    print("eggs: frying...")
    await asyncio.sleep(3) # 2: pause, another tasks can be run
    print("eggs: ready")

async def main():  # 1
    start = time()
    # Run tasks concurrently
    await asyncio.gather(
        make_coffee(),
        fry_eggs()
    )
    print(f"breakfast is ready in {time()-start} min")

asyncio.run(main())  # run top-level function concurrently

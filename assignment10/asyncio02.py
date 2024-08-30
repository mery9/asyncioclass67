# example of using an asyncio queue without blocking
from random import random
import asyncio
import time

# coroutine to generate work
async def producer(queue):
    start_time_producer = time.perf_counter()
    print('Producer: Running')
    # generate work
    for i in range(10):
        # generate a value
        value = i

        # block to simulate work
        # sleeptime = random()
        sleeptime = 0.3

        print(f"> Producer {value} sleep {sleeptime}")
        await asyncio.sleep(sleeptime)
        # add to the queue
        print(f"> Producer put {value}")
        await queue.put(value)
    # send an all done signal
    await queue.put(None)
    print('Producer: Done')
    end_time_producer = time.perf_counter()
    print(f"Time taken for producer : {end_time_producer-start_time_producer} seconds")

 
# coroutine to consume work
async def consumer(queue):
    start_time_consumer = time.perf_counter()
    print('Consumer: Running')
    # consume work
    while True:
        # get a unit of work without blocking
        try:
            item = queue.get_nowait()
        except asyncio.QueueEmpty:
            print('Consumer: got nothing, waiting a while...')
            await asyncio.sleep(0.5)
            continue
        # check for stop
        if item is None:
            break
        # report
        print(f'\t> Consumer got {item}')
    # all done
    print('Consumer: Done')
    end_time_consumer = time.perf_counter()
    print(f"Time taken for consumer : {end_time_consumer-start_time_consumer} seconds")
 
# entry point coroutine
async def main():
    start_time_main = time.perf_counter()
    # create the shared queue
    queue = asyncio.Queue(maxsize=0)
    # run the producer and consumers
    await asyncio.gather(producer(queue), consumer(queue))
    end_time_main = time.perf_counter()
    print(f"Time taken for all : {end_time_main-start_time_main} seconds")
 
# start the asyncio program
asyncio.run(main())
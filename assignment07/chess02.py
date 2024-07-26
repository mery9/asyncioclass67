import asyncio
import time

my_compute_time = 0.1
opponent_compute_time = 0.5
opponents = 24
move_pairs = 30

# Again notice that I declare the main() function as a async function
async def main(x):
    start_counter = time.perf_counter()
    for i in range (move_pairs):
        # print(f"Board-{x} {i+1} Judit thinking of making a move")
        # Don't use time.sleep in a async function. I'm using it because in reality you aren't thinking about
        # move on 24 boards at the same time, and so I need to block the event loop
        time.sleep(my_compute_time)
        print(f"Board - {x+1} {i+1} Judit made a move")
        # Here our opponent is making their turn and now we can move onto the next board.
        await asyncio.sleep(opponent_compute_time)
        print(f"Board - {x+1} {i+1} Opponent made a move")
    print(f"Board - {x+1} >>>>>>>>>>>>>>> Finished move in {round(time.perf_counter() - start_counter)}")
    return round(time.perf_counter() - start_counter)

async def async_io():
    # Again same structure as in async-io.py
    tasks = []
    for i in range(opponents):
        tasks += [main(i)]
    await asyncio.gather(*tasks)
    print(f"Board exhibition finished in {round(time.perf_counter() - start_time)} secs.")


if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(async_io())
    print(f"Finished in {round(time.perf_counter() - start_time)} secs.")
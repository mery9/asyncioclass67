import time
import asyncio

data1 = [5, 2, 3, 1, 4]
data2 = [50, 30, 10, 20, 40]
data3 = [500, 300, 100, 200, 400]

async def process_data(data, delay):
    start = time.perf_counter()
    print(f"At t={time.perf_counter()-start:.2f} รอ {delay} วินาทีก่อนประมวลผลข้อมูลชุดนี้...")
    await asyncio.sleep(delay)

    sorted_data = sorted(data)

    print(f"At t={time.perf_counter()-start:.2f} ข้อมูลที่เรียงลำดับ: {sorted_data}")
    return sorted_data


async def main():
    start = time.perf_counter()
    result1 = process_data(data1, 2)
    result2 = process_data(data2, 3)
    result3 = process_data(data3, 1)
    await asyncio.gather(result1, result2, result3)


    print(f"At t={time.perf_counter()-start:.2f} ผลลัพธ์จาก data1: {result1}")
    print(f"At t={time.perf_counter()-start:.2f} ผลลัพธ์จาก data2: {result2}")
    print(f"At t={time.perf_counter()-start:.2f} ผลลัพธ์จาก data3: {result3}")

# Running the async main function
asyncio.run(main())




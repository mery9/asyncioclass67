import time

data1 = [5, 2, 3, 1, 4]
data2 = [50, 30, 10, 20, 40]
data3 = [500, 300, 100, 200, 400]

def process_data(data, delay):
    print(f"At t={time.time()-start:.2f} รอ {delay} วินาทีก่อนประมวลผลข้อมูลชุดนี้...")
    time.sleep(delay)

    sorted_data = sorted(data)

    print(f"At t={time.time()-start:.2f} ข้อมูลที่เรียงลำดับ: {sorted_data}")
    return sorted_data

start = time.time()
result1 = process_data(data1, 2)
result2 = process_data(data2, 3)
result3 = process_data(data3, 1)

print(f"At t={time.time()-start:.2f} ผลลัพธ์จาก data1: {result1}")
print(f"At t={time.time()-start:.2f} ผลลัพธ์จาก data2: {result2}")
print(f"At t={time.time()-start:.2f} ผลลัพธ์จาก data3: {result3}")

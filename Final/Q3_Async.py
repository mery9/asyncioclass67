import random
import time
import asyncio

class SolarCell:
    def __init__(self, id):
        self.id = id
        self.hardware_readtime = random.randint(1, 3)
        print(f"Solar Cell {id} hardware speed: {self.hardware_readtime}")

    async def read_voltage(self):
        voltage = round(random.uniform(3.2, 6.0), 2)
        await asyncio.sleep(self.hardware_readtime)
        return voltage

async def read_from_solar_cell(solar_cells):
    try:
        while True:
            for solar_cell in solar_cells:
                voltage = await solar_cell.read_voltage()
                print(f"{time.ctime()} Solar Cell #{solar_cell.id} Voltage: {voltage} V")
    except KeyboardInterrupt:
        print("\nโปรแกรมหยุดทำงาน")

async def main():
    num_cells = 5
    print(f"จำนวนแผงโซล่าเซลที่สร้าง: {num_cells}")
    solar_cells = [SolarCell(i + 1) for i in range(num_cells)]
    await asyncio.gather(read_from_solar_cell(solar_cells))

# Running the async main function
asyncio.run(main())






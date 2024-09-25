import random
import time

class SolarCell:
    def __init__(self, id):
        self.id = id
        self.hardware_readtime = random.randint(1,3)
        print(f"Solat Cell {id} hardware speed: {self.hardware_readtime}")

    def read_voltage(self):
        voltage = round(random.uniform(3.2, 6.0), 2)
        time.sleep(self.hardware_readtime)
        return voltage

def read_from_solar_cell(solar_cells):
    try:
        while True:
            for solar_cell in solar_cells:
                voltage = solar_cell.read_voltage()
                print(f"{time.ctime()} Solar Cell #{solar_cell.id} Voltage: {voltage} V")
    except KeyboardInterrupt:
        print("\nโปรแกรมหยุดทำงาน")

if __name__ == "__main__":
    num_cells = 1
    print(f"จำนวนแผงโซล่าเซลที่สร้าง: {num_cells}")

    solar_cells = [SolarCell(i+1) for i in range(num_cells)]
    read_from_solar_cell(solar_cells)
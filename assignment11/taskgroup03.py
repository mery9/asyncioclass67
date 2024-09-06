import time
import asyncio
from asyncio import Queue, TaskGroup

class Product:
    def __init__(self, product_name: str, base_checkout_time: float):
        self.product_name = product_name
        self.base_checkout_time = base_checkout_time

class Customer:
    def __init__(self, customer_id: int, products: list[Product]):
        self.customer_id = customer_id
        self.products = products

async def checkout_customer(queue: Queue, cashier_number: int):
    cashier_total_time = 0  # Initialize cashier's total time
    cashier_start_time = time.perf_counter()  # Start time for the cashier
    customer_count = 0  # Count how many customers this cashier checks out

    while not queue.empty():
        customer: Customer = await queue.get()
        customer_start_time = time.perf_counter()
        print(f"The Cashier_{cashier_number} will checkout Customer_{customer.customer_id}")

        for product in customer.products:
            # If cashier is cashier_2, use fixed checkout time 0.1 for all products
            if cashier_number == 2:
                adjusted_checkout_time = 0.1
            else:
                # Adjust checkout time based on cashier number using formula 1 + (0.1 * cashier_number)
                adjusted_checkout_time = product.base_checkout_time + (0.1 * cashier_number)
            
            print(f"The Cashier_{cashier_number} "
                  f"will checkout Customer_{customer.customer_id}'s "
                  f"Product_{product.product_name} "
                  f"in {adjusted_checkout_time} secs")
            await asyncio.sleep(adjusted_checkout_time)
        
        customer_checkout_time = time.perf_counter() - customer_start_time
        cashier_total_time += customer_checkout_time  # Add to cashier's total time
        print(f"The Cashier_{cashier_number} finished checkout Customer_{customer.customer_id} "
              f"in {round(customer_checkout_time, ndigits=2)} secs")

        customer_count += 1  # Increment customer count
        queue.task_done()

    # After all customers are processed, return the total time and customer count for the cashier
    cashier_total_time = time.perf_counter() - cashier_start_time
    return cashier_number, customer_count, round(cashier_total_time, ndigits=2)

def generate_customer(customer_id: int) -> Customer:
    # Base checkout times for products
    all_products = [Product('beef', 1),
                    Product('banana', .4),
                    Product('sausage', .4),
                    Product('diapers', .2)]
    return Customer(customer_id, all_products)

async def customer_generation(queue: Queue, customers: int):
    customer_count = 0
    while True:
        customers = [generate_customer(the_id)
                     for the_id in range(customer_count, customer_count + customers)]
        for customer in customers:
            print("waiting to put customer in line...")
            await queue.put(customer)
            print("Customer put in line...")
        customer_count = customer_count + len(customers)
        await asyncio.sleep(.001)
        return customer_count

async def main():
    number_of_cashiers = 5
    
    customer_queue = Queue(3)
    customers_start_time = time.perf_counter()

    async with TaskGroup() as group:
        customer_producer = group.create_task(customer_generation(customer_queue, 10))
        cashiers = [group.create_task(checkout_customer(customer_queue, i)) for i in range(number_of_cashiers)]
    
    print("---------------------")
    for cashier in cashiers:
        cashier_number, customers, total_time = cashier.result()
        print(f"The Cashier_{cashier_number} took {customers} customers total {total_time} secs")

    print(f"The supermarket process finished {customer_producer.result()} customers "
          f"in {round(time.perf_counter() - customers_start_time, ndigits=2)} secs")

if __name__ == "__main__":
    asyncio.run(main())

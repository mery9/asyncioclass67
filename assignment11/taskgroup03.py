import time
import asyncio
from asyncio import Queue, TaskGroup
from random import randrange

# we first implement the Customer and Product classes, 
# representing customers and products that need to be checked out. 
# The Product class has a checkout_time attribute, 
# which represents the time required for checking out the product.
class Product:
    def __init__(self, product_name: str, checkout_time: float):
        self.product_name = product_name
        self.checkout_time = checkout_time

class Customer:
    def __init__(self, customer_id: int, products: list[Product]):
        self.customer_id = customer_id
        self.products = products

# we implement a checkout_customer method that acts as a consumer.
# As long as there is data in the queue, this method will continue to loop. 
# During each iteration, it uses a get method to retrieve a Customer instance. 
# 
# If there is no data in the queue, it will wait. 
# 
# After retrieving a piece of data (in this case, a Customer instance), 
# it iterates through the products attribute and uses asyncio.sleep to simulate the checkout process.
# 
# After finishing processing the data, 
# we use queue.task_done() to tell the queue that the data has been successfully processed.
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
                adjusted_checkout_time = product.checkout_time + (0.1 * cashier_number)
            
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


# we implement the generate_customer method as a factory method for producing customers.
#
# We first define a product series and the required checkout time for each product. 
# Then, we place 0 to 4 products in each customer’s shopping cart.
def generate_customer(customer_id: int) -> Customer:
    all_products = [Product('beef', 1),
                    Product('banana', .4),
                    Product('sausage', .4),
                    Product('diapers', .2)]
    return Customer(customer_id, all_products)

# we implement the customer_generation method as a producer. 
# This method generates several customer instances regularly 
# and puts them in the queue. If the queue is full, the put method will wait.
async def customer_generation(queue: Queue, customers: int):
    customer_count = 0
    while True:
        customers = [generate_customer(the_id)
                     for the_id in range(customer_count, customer_count + customers)]
        for customer in customers:
            print(f"Waiting to put Customer_{customer.customer_id} in line.... ")
            await queue.put(customer)
            print(f"Customer_{customer.customer_id} put in line...")
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

# https://aiokafka.readthedocs.io/en/stable/

from aiokafka import AIOKafkaProducer
import asyncio

async def send_messages():
    producer = AIOKafkaProducer(bootstrap_servers='192.168.137.1:9092')
    await producer.start()
    try:
        counter = 1
        while True:
            message = f"Super message from producer1 {counter}".encode('utf-8')
            respone = await producer.send_and_wait("my_topic", message)
            print(respone)
            print(f"Sent: {message.decode('utf-8')}")
            counter += 1
            await asyncio.sleep(0.1)  # Wait for 3 seconds before sending the next message
    finally:
        await producer.stop()


asyncio.run(send_messages())

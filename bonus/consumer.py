# https://aiokafka.readthedocs.io/en/stable/

from aiokafka.admin import AIOKafkaAdminClient, NewTopic
from aiokafka import AIOKafkaConsumer
import asyncio

async def create_topic():
    admin_client = AIOKafkaAdminClient(bootstrap_servers='localhost:9092')
    await admin_client.start()
    try:
        # Check if the topic exists, otherwise create it
        existing_topics = await admin_client.list_topics()
        if 'my_topic' not in existing_topics:
            topic = NewTopic(name="my_topic", num_partitions=3, replication_factor=3)
            await admin_client.create_topics([topic])
            print("Topic 'my_topic' created with replication factor 3.")
    finally:
        await admin_client.close()  # Replace stop() with close()

async def consume():
    consumer = AIOKafkaConsumer(
        'my_topic', 'my_other_topic',
        bootstrap_servers='localhost:9092',
        group_id="my-group")
    await consumer.start()
    try:
        async for msg in consumer:
            print("consumed: ", msg.topic, msg.partition, msg.offset,
                  msg.key, msg.value, msg.timestamp)
    finally:
        await consumer.stop()

async def main():
    await create_topic()
    await consume()

asyncio.run(main())


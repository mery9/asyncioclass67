from kafka.admin import KafkaAdminClient, NewTopic
from kafka.errors import TopicAlreadyExistsError

def create_kafka_topic(bootstrap_servers, topic_name, num_partitions, replication_factor):
    admin_client = KafkaAdminClient(
        bootstrap_servers=bootstrap_servers,
        client_id='kafka-topic-creator'
    )

    topic_list = []
    topic_list.append(NewTopic(name=topic_name, num_partitions=num_partitions, replication_factor=replication_factor))

    try:
        admin_client.create_topics(new_topics=topic_list, validate_only=False)
        print(f"Topic '{topic_name}' created successfully.")
    except TopicAlreadyExistsError:
        print(f"Topic '{topic_name}' already exists.")
    except Exception as e:
        print(f"An error occurred while creating the topic: {str(e)}")
    finally:
        admin_client.close()

if __name__ == "__main__":
    # Kafka broker addresses
    bootstrap_servers = ['kafka:9092', 'kafka2:9092', 'kafka3:9092']

    # Topic configuration
    topic_name = "my_topic"
    num_partitions = 1  # You can adjust this as needed
    replication_factor = 3  # This will create 3 replicas across the brokers

    create_kafka_topic(bootstrap_servers, topic_name, num_partitions, replication_factor)
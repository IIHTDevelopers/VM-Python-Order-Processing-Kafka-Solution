import json
from confluent_kafka import Producer


def load_data_from_json(file_path):
    """Load orders from the provided JSON file."""
    with open(file_path, 'r') as f:
        return json.load(f)


def acked(err, msg):
    """Delivery callback to check if the message was successfully delivered or not."""
    if err is not None:
        print(f"Failed to deliver message: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [Partition: {msg.partition()}]")


def produce_orders(data, topic='order_topic'):
    """Produce orders to Kafka with a fixed partitioning strategy (2 partitions)."""
    producer = Producer({'bootstrap.servers': 'localhost:9092'})

    for order in data:
        value = json.dumps(order)

        # Assign messages with even order_id to partition 0, and odd order_id to partition 1
        partition = 0 if int(order['order_id']) % 2 == 0 else 1

        # Produce the message to a specific partition
        producer.produce(topic, value=value, partition=partition, callback=acked)

        # Poll for delivery report callbacks
        producer.poll(1)

    # Wait for any outstanding messages to be delivered and delivery report callbacks to be triggered
    producer.flush()


if __name__ == "__main__":
    # Load data from JSON file and send to Kafka topic
    data = load_data_from_json('dataset.json')
    produce_orders(data)

from kafka import KafkaProducer


# poetry add kafka-python
def produce_kafka():
    brokers = ['localhost:29092', 'localhost:39092']
    topics = ['test-topic', 'test1-topic']

    producer = KafkaProducer(bootstrap_servers=brokers)

    for _ in range(3):
        for each_topic in topics:
            producer.send(each_topic, b'Hello, World!')
            producer.flush()
    
    
if __name__ == "__main__":
    produce_kafka()
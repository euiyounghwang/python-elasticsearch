from kafka import KafkaProducer



def produce_kafka():
    brokers = ['localhost:29092', 'localhost:39092']
    topic = 'test-topic'

    producer = KafkaProducer(bootstrap_servers=brokers)

    for _ in range(3):
        producer.send(topic, b'Hello, World!')
        producer.flush()
    
    
if __name__ == "__main__":
    produce_kafka()
from kafka import KafkaConsumer


# poetry add kafka-python
def consumer_kafka():
    brokers = ['localhost:29092', 'localhost:39092']
    topic = 'test-topic'

    consumer = KafkaConsumer(topic, group_id="Python_Kafka_Consumer_Job", bootstrap_servers=brokers)

    for message in consumer:
        print(message, message.value, message.value.decode("utf-8"))
    
    
        
if __name__ == "__main__":
    consumer_kafka()
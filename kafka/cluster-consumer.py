from kafka import KafkaConsumer

brokers = ['localhost:29092', 'localhost:39092']
topic = 'test-topic'

consumer = KafkaConsumer(topic, bootstrap_servers=brokers)

for message in consumer:
    print(message, message.value, message.value.decode("utf-8"))
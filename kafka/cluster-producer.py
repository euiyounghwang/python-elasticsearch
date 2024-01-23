from kafka import KafkaProducer

brokers = ['localhost:29092', 'localhost:39092']
topic = 'test-topic'

producer = KafkaProducer(bootstrap_servers=brokers)

producer.send(topic, b'Hello, World!')
producer.flush()
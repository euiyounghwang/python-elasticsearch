
#### Kafka Install
```bash
# Monitoring
kafka-monitoring:
    image: obsidiandynamics/kafdrop
    restart: "no"
    ports:
      - "9009:9000"
    environment:
      KAFKA_BROKER_CONNECT: "kafka-1:9092"
    depends_on:
      - kafka-1
      - kafka-2
```

#### Create Topic
```bash
docker exec -it kafka-cluster-kafka-1-1 kafka-topics --bootstrap-server=localhost:9092 --create --topic test-topic --partitions 3 --replication-factor 1
```

#### Kafka Monitoring
![Alt text](../screenshot/kafka-monitoring.png)
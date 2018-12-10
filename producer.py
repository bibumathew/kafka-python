import json

import kafka

import datetime
import time

producer = kafka.KafkaProducer(
    bootstrap_servers="192.168.0.18:9092",
    value_serializer=lambda m: json.dumps(m).encode("ascii"),
)

for event in range(100):
    topics = 'test'
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    producer.send(topics, {"key": st})

producer.flush()

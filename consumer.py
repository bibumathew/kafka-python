import json

import kafka

consumer = kafka.KafkaConsumer(
    bootstrap_servers="127.0.0.1:9092",
    group_id="some_group_id"
)

consumer.subscribe(['test'])

for message in consumer:
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                         message.offset, message.key,
                                         message.value))

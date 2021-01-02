from kafka import KafkaConsumer
import json

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('com.udacity.apache.spark.police.service-calls',
                         bootstrap_servers=['localhost:9092'],
                         auto_offset_reset='earliest', 
                         enable_auto_commit=False,
                         value_deserializer=lambda m: json.loads(m.decode('ascii'))
                        )

#Print messages from consumer
for message in consumer:
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition, message.offset, message.key, message.value))
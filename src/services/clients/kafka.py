import logging
import sys
from typing import Callable
from confluent_kafka import KafkaError, Producer, Consumer, KafkaException
import uuid

import constants

def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))

class KafkaClient:
    def __init__(self):
        self.host = constants.KAFKA_1_HOST
        self.port = constants.KAFKA_1_PORT
        self.running = True
        self.producers = {}
        self.consumers = {}

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            handlers=[logging.FileHandler("debug.log"), logging.StreamHandler(sys.stdout)],
        )
        self.logger = logging.getLogger(__name__)

    def create_producer(self, key: str):
        conf = {
            "bootstrap.servers": f"{self.host}:{self.port}",
            "client.id": "ciwallet-bot"
        }
        self.producers[key] = Producer(conf)
        return self.producers[key]
    
    def create_consumer(self, key: str, group_id: str):
        conf = {
            "bootstrap.servers": f"{self.host}:{self.port}",
            "client.id": "ciwallet-bot",
            "group.id": group_id,
            "auto.offset.reset": "earliest"
        }
        self.consumers[key] = Consumer(conf)
        return self.consumers[key]

    def produce(self, key: str, topic: str, message: str):
        producer = self.producers[key]
        if not producer:
            raise Exception("Producer not created")
        try:
            producer.produce(topic, key=uuid.uuid4().__str__(), value=message, callback=acked)
        except KafkaException as e:
            self.logger.error(f"Failed to produce message: {e}")

    def basic_consume_loop(self, key: str, topic: str, callback: Callable[[str], None]):
        consumer = self.consumers[key]
        if not consumer:
            raise Exception("Producer not created")
        try:
            consumer.subscribe(topic)
            while self.running:
                msg = consumer.poll(timeout=1.0)
                if msg is None: continue

                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        self.logger.error('%% %s [%d] reached end at offset %d\n' %
                                        (msg.topic(), msg.partition(), msg.offset()))
                    elif msg.error():
                        raise KafkaException(msg.error())
                else:
                    callback(msg)
        finally:
            consumer.close()


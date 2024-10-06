import logging
from os import error
import sys
from typing import Callable
from confluent_kafka import KafkaError, Producer, Consumer, KafkaException
import uuid

import constants

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

    def create_producer(self, id: str = constants.DEFAULT_ID):
        conf = {
            "bootstrap.servers": f"{self.host}:{self.port}",
            "client.id": "ciwallet-bot"
        }
        self.producers[id] = Producer(conf)
        return self.producers[id]
    
    def create_consumer(
            self, 
            id: str = constants.DEFAULT_ID, 
            group_id: str = constants.DEFAULT_GROUP_ID):
        conf = {
            "bootstrap.servers": f"{self.host}:{self.port}",
            "client.id": "ciwallet-bot",
            "group.id": group_id,
            "auto.offset.reset": "earliest"
        }
        self.consumers[id] = Consumer(conf)
        return self.consumers[id]

    def acked(self, err: error, msg: str):
        if err is not None:
            self.logger.error("Failed to deliver message: %s: %s" % (str(msg), str(err)))
        else:
            self.logger.info("Message produced: %s" % (str(msg)))

    def produce(self, topic: str, message: str, id: str = constants.DEFAULT_ID):
        producer = self.producers[id]
        if not producer:
            raise Exception("Producer not created")
        try:
            producer.produce(topic=topic, value=message, callback=self.acked)
        except KafkaException as e:
            self.logger.error(f"Failed to produce message: {e}")

    def basic_consume_loop(self, topic: str, callback: Callable[[str], None], id: str = constants.DEFAULT_ID):
        consumer = self.consumers[id]
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


from confluent_kafka import Producer
import json
import configparser

def create_kafka_producer(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    
    kafka_conf = {
        "bootstrap.servers": config.get("kafka", "bootstrap_servers")
    }
    
    producer = Producer(kafka_conf)
    return producer

def produce_to_kafka(producer, topic, data):
    producer.produce(topic, json.dumps(data))
    producer.flush()
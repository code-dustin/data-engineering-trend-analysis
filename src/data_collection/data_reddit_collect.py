from data_praw import create_reddit_instance, get_subreddit_posts
from data_kafka_producer import create_kafka_producer, produce_to_kafka
import time
import configparser

def main():
    config_file = "config/config.ini"
    config = configparser.ConfigParser()
    config.read(config_file)
    topic = config.get("kafka", "topic")
    
    reddit = create_reddit_instance(config_file)
    producer = create_kafka_producer(config_file)
    
    while True:
        try:
            posts = get_subreddit_posts(reddit, "dataengineering", limit=10)
            for post in posts:
                produce_to_kafka(producer, topic, post.title)
            time.sleep(60)
        except Exception as e:
            print(f"Error has occurred: {e}")
            time.sleep(60)

if __name__ == "__main__":
    main()
import praw
import configparser

def create_reddit_instance(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    
    reddit = praw.Reddit(
        client_id=config.get("reddit", "client_id"),
        client_secret=config.get("reddit", "client_secret"),
        user_agent=config.get("reddit", "user_agent"),
        username=config.get("reddit", "username"),
        password=config.get("reddit", "password"),
    )
    
    return reddit

def get_subreddit_posts(reddit, subreddit_name, limit=100):
    subreddit = reddit.subreddit(subreddit_name)
    posts = []
    for submission in subreddit.new(limit=limit):
        posts.append(submission)
    
    return posts

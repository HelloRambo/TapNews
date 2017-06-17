# -*- coding: utf-8 -*-

import os
import sys
from newspaper import Article

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

from cloudAMQP_client import CloudAMQPClient


# queue which scraper put the news
SCRAPE_NEWS_TASK_QUEUE_URL = "amqp://nklrrnkw:ZRRNkXKVSmrC-8EKvQU2CxPXkbkDp5Bl@fish.rmq.cloudamqp.com/nklrrnkw"
SCRAPE_NEWS_TASK_QUEUE_NAME = "tap-news"

# handle news, then store in deduper queue
DEDUPER_NEWS_TASK_QUEUE_URL = "amqp://bbyeamhc:T93ctHhXadQbMQIM7pFHELOC0rZ7cmmC@fish.rmq.cloudamqp.com/bbyeamhc"
DEDUPER_NEWS_TASK_QUEUE_NAME = "news_for_deduper"

SLEEP_TIME_IN_SECONDS = 5

deduper_news_queue_client = CloudAMQPClient(DEDUPER_NEWS_TASK_QUEUE_URL, DEDUPER_NEWS_TASK_QUEUE_NAME)
scrape_news_queue_client = CloudAMQPClient(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)

def handle_message(msg):
    if msg is None or not isinstance(msg, dict):
        print 'message is broken'
        return 
    task = msg

    # use newspaper to substitute xpath
    article = Article(task['url'])
    article.download()
    article.parse()
    task['text'] = article.text
    print "*************** task['text']:" ,task['text']
    deduper_news_queue_client.sendMessage(task)

while True:
    # fetch msg from queue which scraper put news at
    # handle message, store in another queue
    if scrape_news_queue_client is not None:
        msg = scrape_news_queue_client.getMessage()
        if msg is not None:
            # handle message
            try:
                handle_message(msg)
            except Exception as e:
                print e
                pass

        scrape_news_queue_client.sleep(SLEEP_TIME_IN_SECONDS)

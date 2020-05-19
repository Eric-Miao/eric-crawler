""" 
import threading
from queue import Queue
from spider import Spider
from domain import *
from file_processor import *

NUM_OF_THREADS = 4
project_name = None
home_page = None
domain_name = None

waiting_queue_file = None
crawled_queue_file = None

queue = Queue()


def crawl():
    waiting_links = file_to_set(waiting_queue_file)
    if len(waiting_links) > 0:
        create_jobs()

# Each queued link is a new job
def create_jobs():
    for link in file_to_set(waiting_queue_file):
        queue.put(link)
    queue.join()
    crawl()

# Create worker threads (will die when main exits)
def create_workers():
    for _ in range(NUM_OF_THREADS):
        t = threading.Thread(target = work)
        t.daemon = True
        t.start()

# Tell the workers to do the next job in the queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()

if __name__ == '__main__':
    # Get the project name from user
    project_name = input('tell me the name of your project: ')
    # Home page from user
    home_page = input('tell me the homepage of your target: ')
    # Get the domain name of our home page.
    domain_name = get_domain_name(home_page)
    
    want_multi_thread = True if input('Do you want to do the job multi_thread? y/n')=='y' else False
    
    waiting_queue_file = project_name + '/waiting_queue.txt'
    crawled_queue_file = project_name + '/crawled_queue.txt'

    Spider(project_name, home_page, domain_name)

    if want_multi_thread:
        create_workers()
        crawl()

 """
import spider

if __name__ == '__main__':
    root_url = input('tell me the root url of target: ')
    spider = spider.Spider(root_url)
    spider.start()
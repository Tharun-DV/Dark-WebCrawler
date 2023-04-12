import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *
from torbootstrap import *
process()
bootstarp()
PROJECT_NAME = input("Enter Project Name:")
HOMEPAGE = input("Enter Url:")
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + "/notyetcrawled.txt"
CRAWLED_FILE = PROJECT_NAME + "/crawled.txt"
print(f"No of Threads Currently Running {threading.active_count()}")
NUMBER_OF_THREADS = int(input("Enter No. of Theads to Be used :"))

queue = Queue()
Spider(PROJECT_NAME,HOMEPAGE,DOMAIN_NAME)


def create_jobs():
    for links in convert_file_to_set(QUEUE_FILE):
        queue.put(links)
    queue.join()
    crawl()


def crawl():
    queued_links = convert_file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(f"{str(len(queued_links))} links yet to be crawled")
        create_jobs()

def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name,url)
        queue.task_done()


create_workers()
crawl()
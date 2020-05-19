from urllib.request import urlopen
from link_finder import LinkFinder
import file_processor

class Spider:

    # Class vairables share among all instances (in case of multi-thread)   
    project_name = ''
    base_url = ''
    domain_name = ''
    waiting_queue_file = ''
    crawled_queue_file = ''
    waiting_queue = set()
    crawled_queue = set()

    def __init__(self, proj_name, base_url, domain_name):
        Spider.project_name = proj_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.waiting_queue_file = Spider.project_name + '/waiting_queue.txt'
        Spider.crawled_queue_file = Spider.project_name + '/crawled_queue.txt'
        self.boot()
        self.crawl_page('First spider', Spider.base_url)        

    @staticmethod
    def boot():
        file_processor.create_project_dir(Spider.project_name)
        file_processor.create_data_files(Spider.project_name, Spider.base_url)
        Spider.waiting_queue = file_processor.file_to_set(Spider.waiting_queue_file)
        Spider.crawled_queue = file_processor.file_to_set(Spider.crawled_queue_file)

    @staticmethod
    def crawl_page(name, page_url):
        if page_url not in Spider.crawled_queue:
            print(name + ' now crawling ' + page_url)
            print('Waiting ' + str(len(Spider.waiting_queue)) + ' | Crawled ' + str(len(Spider.crawled_queue)))
            Spider.add_links_to_waiting_queue(Spider.gather_links(page_url))
            Spider.waiting_queue.remove(page_url)
            Spider.crawled_queue.add(page_url)
            Spider.update_files()

    @staticmethod
    def fetch_website(page_url):
        reponse = urlopen(page_url)
        if reponse.getheader('Content-Type') == 'text/html':
            html_bytes = reponse.read()
            html_string = html_bytes.decode('utf-8')
        return html_string

    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            html_string = Spider.fetch_website(page_url)
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
        except:
            print('Error: cannot crawl page')
            return set()
        return finder.page_links()
    
    @staticmethod
    def add_links_to_waiting_queue(links):
        Spider.add_links_to_queue(links, 'waiting')
    
    @staticmethod
    def add_links_to_crawled_queue():
        pass
    
    @staticmethod
    def add_links_to_queue(links, queue):
        if queue == 'waiting':
            for url in links:
                if url in Spider.waiting_queue:
                    continue
                if url in Spider.crawled_queue:
                    continue
                # In case the crawler does not go out of the target webset
                if Spider.domain_name not in url:
                    continue
                Spider.waiting_queue.add(url)
    @staticmethod
    def update_files():
        file_processor.set_to_file(Spider.waiting_queue, Spider.waiting_queue_file)
        file_processor.set_to_file(Spider.crawled_queue, Spider.crawled_queue_file)


class UrlManager:

    def __init__(self):
        self.waiting_queue = set()
        self.crawled_queue = set()

    def add_new_url(self, url):

        if not url:
            return
        
        if url in self.waiting_queue:
            return
        
        if url in self.crawled_queue:
            return
        
        self.waiting_queue.add(url)

    def add_new_urls(self, urls):
        for url in urls:
            self.add_new_url(url)


    def get_new_url(self):
        new_url = self.waiting_queue.pop()
        self.crawled_queue.add(new_url)
        return new_url
    
    def has_new_url(self):
        return (len(self.waiting_queue) != 0)
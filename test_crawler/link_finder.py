from html.parser import HTMLParser
from urllib import parse


class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        print('here is the tag we found '+ tag)
        if tag == 'a':
            for (attribute, target_url) in attrs:
                if attribute == 'href':
                    # Use joinurl to solve the relative url
                    url = parse.urljoin(self.base_url, target_url)
                    self.links.add(url)

    def page_links(self):
        return self.links

    def error(self, message):
        pass

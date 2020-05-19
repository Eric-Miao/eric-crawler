from bs4 import BeautifulSoup as bs
from urllib import parse

class HtmlParser:


    def _get_new_urls(self, page_url, soup):

        new_urls = set()
        links = soup.find_all('a')

        for link in links:
            new_url = link['href']
            new_full_url = parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
            print('find new url %s' %(new_full_url))
        print('am i here?')
        return new_urls

    def _get_new_data(self, page_url, soup):
        ret_data = {}

        ret_data['url'] = page_url
        print('ret_data[\'url\'] is ', page_url)
        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>菰</h1>
        title_node = soup.find('dd', class_ = 'lemmaWgt-lemmaTitle-title').find('h1')
        ret_data['title'] = title_node.get_text()
        print('ret_data[\'title\'] is ', ret_data['title'])

        summary_node = soup.find('div', class_ = 'lemma-summary')
        ret_data['summary'] = summary_node.get_text()
        print('ret_data[\'summary\'] is ', ret_data['summary'])
        return ret_data

    def parse(self, page_url, html_cont):

        print('now in parser')
        if not page_url:
            return
        if not html_cont:
            return 
        soup = bs(html_cont, 'html.parser', from_encoding='utf-8')
        print('soup initialized')
        new_urls = self._get_new_urls(page_url, soup)
        print('new_urls extracted')
        new_data = self._get_new_data(page_url, soup)
        print('new_data extracted')
        return new_urls,new_data
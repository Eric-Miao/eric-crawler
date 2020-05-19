from urllib.request import urlopen

class HtmlDownloader:

    def download(self, url):
        if not url:
            return
        
        response = urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()


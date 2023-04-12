from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):

    def error(self, message):
        pass

    def __init__(self,BASE_URL,PAGE_URL):
        super().__init__()
        self.base_url = BASE_URL
        self.page_url = PAGE_URL
        self.links = set()

    def handle_starttag(self, tag,attrs):
        if tag == 'a':
            for (attribute,value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url,value)
                    self.links.add(url)

    def page_links(self):
        return self.links


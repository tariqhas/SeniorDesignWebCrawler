from CrawlerInterface import *

class CrawlerController:

    def __init__(self):
        pass

    def selectAttributes(self, attributeList):
        self.local = LocalCrawler(attributeList)
        self.http = HttpCrawler(attributeList)
        pass

    def crawlDocuments(self, documentList, attributeList):
        self.selectAttributes(attributeList)
        fullData = []
        for doc in documentList:
            protocol = doc[0]
            url = doc[1]
            if protocol == "local":
                self.local.crawl(url)
            else:
                self.http.crawl(url)
        for d in self.local.getData():
            fullData.append(d)
        for d in self.http.getData():
            fullData.append(d)
        return fullData

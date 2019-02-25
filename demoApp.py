# For demonstrating functionality on a limited use case
from AttributeGenerator import *
from DocumentGenerator import *
from DataExportInterface import *
from CrawlerInterface import *

attributeparser = AttributeFileParser('Attributes/wikipediaLocations.txt')
urlparser = URLFileParser('Webpages/wikipediaLocations.txt')
crawler = CrawlerController()
exporter = InformationManager()

atts = attributeparser.read_all_attributes()
urls = urlparser.read_all_urls()
crawlresults = crawler.crawlDocuments(urls, atts)
print(crawlresults)
exporter.createDataframe(crawlresults)
exporter.exportDataframeAsExcel()

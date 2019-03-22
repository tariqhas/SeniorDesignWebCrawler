# For demonstrating functionality on a limited use case
from AttributeGenerator import *
from DocumentGenerator import *
from DataExportInterface import *
from CrawlerInterface import *
from config import *

conf = config
attfilename = 'Attributes/wikipediaLocations.txt'
attributeparser = AttributeFileParser(attfilename)
urlparser = URLFileParser('Webpages/wikipediaLocations.txt')
crawler = CrawlerController()
exporter = InformationManager(conf.local_db)

atts = attributeparser.read_all_attributes()
attid = exporter.addAttributeData(atts, attfilename, "wikipediaatts")
print(attid)

exit()
urls = urlparser.read_all_urls()
crawlresults = crawler.crawlDocuments(urls, atts)

print(crawlresults)
exporter.createDataframe(crawlresults)
exporter.exportDataframeAsExcel()

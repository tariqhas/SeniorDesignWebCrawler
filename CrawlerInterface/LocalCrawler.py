import re
import xml.etree.ElementTree as et


class LocalCrawler:

    def __init__(self, attributes):  # attributes is a list of tuples (attributename, ruletype, regex/xpath)
        self.attributes = attributes
        self.fulldata = {}
        pass

    def crawl(self, url):  # URL must be an absolute path
        urldata = {}
        try:
            with open(url, mode='r') as fin:
                filetext = fin.read()
                for a in self.attributes:
                    name, rtype, patt = a
                    if rtype=='regex':
                        try:
                            urldata[name] = re.find(patt, filetext)
                        except Exception as e:
                            pass  # TODO handle exception from re.find here if needed
                    elif rtype=='xpath':
                        try:
                            tree = et.parse(url)  # This can also be read from string using et.fromstring(urldata)
                            urldata[name] = et.find(patt)
                        except et.ParseError:
                            pass  # TODO handle parse error
                    else:
                        # invalid attribute data
                        raise Exception(message="Attribute Data Malformed : " + name+ ' ' + rtype + ' ' + patt)
        except FileNotFoundError as e:
            pass  # TODO decide how to handle FNF exception
        self.fulldata[url] = urldata


    def getData(self):
        return self.fulldata

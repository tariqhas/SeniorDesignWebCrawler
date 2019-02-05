from DocumentGenerator import *


class URLFileParser:

    def __init__(self, fin):
        if fin:
            self.filename = fin
        else:
            raise AttributeError(message="Must provide filename to URLFileParser")
        self.urlParser = URLExtractor()
        self.fileEntity = open(self.filename, 'r')  # create readable file object

    def read_single_url(self, urlline):
        protocol = urlline.split(sep=":")[0]
        url = ''.join(urlline.split(sep=":")[1:])
        parsedUrl = self.urlParser.parse(url, protocol)
        return parsedUrl

    def read_all_urls(self):
        urllist = []
        for line in self.fileEntity.readlines():
            urllist.append(self.read_single_url(line))
        return urllist

    def destroy(self):
        # close file reader
        self.fileEntity.close()
        # TODO deal with created extractor objects as needed
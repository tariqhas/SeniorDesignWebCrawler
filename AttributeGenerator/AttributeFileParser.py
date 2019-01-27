from AttributeGenerator import *


class AttributeFileParser:

    def __init__(self, fin):
        if fin:
            self.filename = fin
        else:
            raise AttributeError(message="Must provide filename to AttributeFileParser")
        self.regexParser = RegexExtractor()  # initialize regex processor
        self.attributeParser = AttributeExtractor()  # initialize attribute processor
        self.fileEntity = open(self.filename, 'r')  # create readable file object

    def read_single_attribute(self, attributeline):
        attribute = attributeline.split(sep="|")[0]
        # only first pipe is treated as delimiter, others are treated as part of regex
        regex = ''.join(attributeline.split(sep="|")[1:])
        parsedattribute = self.attributeParser.parse(attribute)
        parsedregex = self.regexParser.parse(regex)
        return parsedattribute, parsedregex

    def read_all_attributes(self):
        attributelist = []
        for line in self.fileEntity.readlines():
            attributelist.append(self.read_single_attribute(line))
        return attributelist

    def destroy(self):
        self.fileEntity.close()

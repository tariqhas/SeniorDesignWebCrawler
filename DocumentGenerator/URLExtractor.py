

class URLExtractor:

    def __init__(self):
        pass

    def parse(self, urlline):
        url = urlline.strip()
        protocol = url.split(sep=":")[0]
        if "file" is in protocol:
            pass  # open local file as document
        else:
            pass  # fetch remote html file

    # Given a line from a file, determine the URL string and the URL type and return them as a tuple
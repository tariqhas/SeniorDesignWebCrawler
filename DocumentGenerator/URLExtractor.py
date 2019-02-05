

class URLExtractor:

    def __init__(self):
        pass

    def parse(self, urlline):
        url = urlline.strip()
        protocol = url.split(sep=":")[0]
        if "file" in protocol:
            return "local", url  # open local file as document
        else:
            return "http", url

    # Given a line from a file, determine the URL string and the URL type and return them as a tuple

import os
from DocumentGenerator import *


def run_test():
    localpath = os.getcwd()+"\localurlfile.html\n"
    testurls = [
        localpath,
        "http://cs.unb.ca/~wsong/lab1.html\n"
        "http://www.google.com\n"
    ]
    expectedresults = [
        ('local', 'C:\\Users\\ividito\\Desktop\\SeniorDesign\\Testing\\localurlfile.html'),
        ('http', 'http://cs.unb.ca/~wsong/lab1.html'),
        ('http', 'http://www.google.com')
    ]
    with open('testurls.txt', 'w') as urlfile:
       urlfile.writelines(testurls)
    urlreader = URLFileParser('testurls.txt')
    assert(urlreader.read_all_urls() == expectedresults)


if __name__ == "__main__":
    run_test()
    print("URL Externalizer Test Successful")

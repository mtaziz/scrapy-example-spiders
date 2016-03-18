from lxml import html
import io
import sys
import re
#from HTMLParser import HTMLParser
from StringIO import StringIO
import json
import requests
import lxml.etree
import lxml.html
import xml.etree.ElementTree as ET

# Let's grab the simple page source.


def main():
    simple_page = open('top_bloggers_linkextraction.html').read()

# Let's open it with LXML so we can play around with xpath.
    simple_tree = html.fromstring(simple_page)
    # result = etree.tostring(page)
    with io.open('test.xml','wb') as f:
    	f.writelines(result)

if __name__ == '__main__':
	main()
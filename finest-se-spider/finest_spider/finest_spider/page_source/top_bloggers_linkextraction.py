from __future__ import (unicode_literals, print_function,
                        absolute_import, division, with_statement)
# from __future__ import with_statement
from lxml import html
import io
import sys
import re
#from HTMLParser import HTMLParser
#!/usr/bin/env python
# encoding: utf-8
# from __future__ import (unicode_literals, print_function,
                        # absolute_import, division)
import codecs
import re
import requests
import sys
from os.path import join, dirname, abspath
from StringIO import StringIO
import json
import requests
import lxml.etree
import lxml.html
import xml.etree.ElementTree as ET

# Let's grab the simple page source.


def main():
    simple_page = open('page_source_topbloggers_original.html').read()

# Let's open it with LXML so we can play around with xpath.
    simple_tree = html.fromstring(simple_page)
    with open('lxml_tree.html', 'w', encoding='utf-8') as openfile_simple:
        openfile_simple.write(str(simple_tree))

    # print simple_tree
    lists = simple_tree.xpath('//div[@class="ser_desc"]')
    # string_lists = 
    # items = []
    # for links in lists:
    #     urls = links.xpath('.//div[@class="ser_desc"]/@href')
    #     return items.append(urls)
    # print lists
    with open('top_bloggers.txt', 'w',encoding='utf-8') as f:
            f.write(str(lists))

    # # result = etree.tostring(page)
    # with io.open('test.xml','wb') as f:
    # 	f.writelines(result)
    # 	for blog_link in sel.xpath('//div[@class="ser_desc"]'):
    #         print "blog_link:%s" % blog_link
    #         # size_urls = "%s" % url
    #     # photo_id = url.split('/')[-2]
    #         item = FinestSpiderItem()
    #     # item['emotion'] = self.emotion
    #         item['Size_Url'] = blog_link.xpath('.//div[@class="ser_desc"]/@href').extract()[0]
    #        


def clean_html(content):
    """
    Take HTML content and return a cleaned root element.
    Removes styles, scripts, comments, links etc. from element
    and its child elements.
    See http://lxml.de/3.4/api/lxml.html.clean.Cleaner-class.html
    """
    # Remove line breaks in HTML; lxml includes these in text_content() otherwise.
    content = re.sub(r'(\r\n|\n|\r)+', ' ', content)
    root = lxml.html.fromstring(content)
    cleaner = lxml.html.clean.Cleaner(style=True)
    cleaned_html = cleaner.clean_html(root)
    for el in cleaned_html.xpath("//p|//br|//div"):
        el.tail = "\n\n" + el.tail if el.tail else "\n\n"
    return cleaned_html

def main():
    """ Read HTML file and output cleaned text from it. """
    content = read_file(sys.argv[1])
    cleaned_html = clean_html(content)
    write_output(sys.argv[2], cleaned_html)


if __name__ == '__main__':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
    main()
# if __name__ == '__main__':
#     main()

# import requests
# from lxml import html
# import urllib2

# def main():
#     with open('IBA Official Cocktails.html') as addrlist:
#         info = addrlist.read()
#         tree = html.fromstring(info)

#     addrs = tree.xpath('//a[@class="modal"]/@href')

#     unknowns = 0

#     for a in addrs:
#         addr = "http://www.iba-world.com%s" % a
#         print addr
#         response = urllib2.urlopen(addr)
#         page = response.read()
#         tree = html.fromstring(page)
#         try:
#             cocktail = tree.xpath('//span[@class="info1"]/text()')[0].replace("'",'')
#             with open('cocktails/%s' % cocktail, 'w')as f:
#                 f.write(page)
#         except:
#             with open('cocktails/unknown%s' % str(unknowns), 'w')as f:
#                 unknowns = unknowns + 1
#                 f.write(page)
#     return

#     tree = html.fromstring(page)

#     print page

# #    cocktail = tree.xpath('//*[@id="official_cocktails"]/div[2]/p[1]/span[1]')
# #    ingredients = tree.xpath('//*[@id="official_cocktails"]/div[2]/ul')

#     cocktail = tree.xpath('//span[@class="info1"]/text()')
#     ingredients = tree.xpath('//li/text()')
#     instr = "".join(tree.xpath('//div[@class="oc_info"]/text()')).replace('\r\n', '')
#     print cocktail
#     print ingredients
#     print instr

# if __name__ == '__main__':
#     main()
#!/usr/bin/env python
# -*-coding:utf-8-*-
from __future__ import division
from bs4 import BeautifulSoup
import io 

def write_urls():
    # results = get_urls('urls_general_blogger_3.csv')
    filename = 'urls_general_blogger_3.csv'
    f = open(filename, 'r').read().split()
    # f = open('')
    # with open('ipython_list3.txt', mode='w', encoding='utf-8') as fwrite:
    with open('ipython_list3.txt', mode='w') as fwrite:
        fwrite.write('\n'.join(str(line) for line in f))
        # fwrite.write('\n'.join(results))
        fwrite.write('\n')
    # fwrite.close()
# with open('/path/to/filename.txt', mode='wt', encoding='utf-8') as myfile:
#     myfile.write('\n'.join(lines))


# def get_urls(filename):
#     f = open(filename, 'r').read().split()
#     urls = []
#     for i in f:
#         urls.append(i)
#         return urls
#     f.close()

if __name__ == '__main__':
    write_urls()

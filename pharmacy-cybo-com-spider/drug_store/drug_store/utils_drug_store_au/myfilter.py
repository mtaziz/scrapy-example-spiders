#!/usr/bin/env python
import os, sys
with open('urls.txt', 'r') as fr:
#    fr_read = fr.read()
#r = [i for i in fr_read]
    start_urls = [url.strip() for url in fr.readlines()]
with open('for_test.txt', 'w') as fw:
    fw.write(str(start_urls))
fr.close()
fw.close()


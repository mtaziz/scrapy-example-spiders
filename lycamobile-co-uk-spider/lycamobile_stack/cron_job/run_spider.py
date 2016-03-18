#/usr/bin/python
# -*- coding: utf-8 -*-

import os

root_directory = '/home/mtaziz/.virtualenvs/scrapydevenv/spider/upwork/lycamobile_stack'

os.chdir(root_directory+'lycamobile_stack')
os.system("scrapy crawl lycamobile")


#!/usr/bin/bash
scrapy crawl hillborough_spider -o hillborough_spider.csv -t csv 
mv hillborough_spider.csv ..
#!/usr/bin/bash
scrapy crawl yellowpagesau -o yellowpagesau.csv -t csv 
mv yellowpagesau.csv ..
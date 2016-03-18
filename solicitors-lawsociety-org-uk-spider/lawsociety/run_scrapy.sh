#!/usr/bin/bash
scrapy crawl uklawsociety -o uklawsociety.csv -t csv 
mv uklawsociety.csv ..
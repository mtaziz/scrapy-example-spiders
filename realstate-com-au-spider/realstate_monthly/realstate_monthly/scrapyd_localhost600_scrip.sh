#!/usr/bin/env bash 
#scrapyd
scrapyd-deploy local-target -p realstate_monthly
curl http://localhost:6800/schedule.json -d project=realstate_monthly -d spider=realstate_monthly_spider \
    -d setting=FEED_URI=/home/mtaziz/.virtualenvs/scrapydevenv/spider/realstate_monthly/realstate_monthly/results/realstate_monthly_spider_scrapyd.csv -d setting=FEED_FORMAT=csv -d setting=JOBDIR=/home/mtaziz/.virtualenvs/spider/realstate_monthly/realstate_monthly


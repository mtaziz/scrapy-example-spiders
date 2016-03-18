#/usr/bin/python
# -*- coding: utf-8 -*-
from crontab import CronTab
#####################################################
### MORE info about python-crontab ##################
### https://pypi.python.org/pypi/python-crontab #####
#####################################################

root_directory = '/home/mtaziz/.virtualenvs/scrapydevenv/spider/upwork/lycamobile_stack'

tab = CronTab(user='mtaziz')

cmd_scrapy = 'python '+root_directory+'cron_job/run_spider.py >/dev/null 2>&1'

############# ADD CRON JOB ##################
cron_scrapy = tab.new(cmd_scrapy)

#Job every 7 days to 9 am
cron_scrapy.setall("0 9 */7 * *")

#WRITE CRON JOB
tab.write()

##SHOW NEW CRON JOB
print tab.render()
##############################################

## DEL CRON JOB#############
#cron_job1 = tab.find_command(cmd_scrapy)

#tab.remove_all(cmd_scrapy)

#Write content crontab
#tab.write()

#print tab.render()
####################################

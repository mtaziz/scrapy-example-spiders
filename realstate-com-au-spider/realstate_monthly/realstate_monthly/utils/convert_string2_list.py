#!/usr/bin/env python
unit_monthly_date = 
unit_mly_p_jan = scrapy.Field unit_mly_p_feb = scrapy.Field unit_mly_p_mar = scrapy.Field unit_mly_p_apr = scrapy.Field unit_mly_p_may = scrapy.Field unit_mly_p_jun = scrapy.Field unit_mly_p_jul = scrapy.Field unit_mly_p_aug = scrapy.Field unit_mly_p_sep = scrapy.Field unit_mly_p_oct = scrapy.Field unit_mly_p_nov = scrapy.Field unit_mly_p_dec = scrapy.Field
#regex: unit\_mly\_p\_[a-z]{3}

unit_mly_date_string = 'unit_mly_jan = scrapy.Field unit_mly_feb = scrapy.Field unit_mly_mar = scrapy.Field unit_mly_apr = scrapy.Field unit_mly_may = scrapy.Field unit_mly_jun = scrapy.Field unit_mly_jul = scrapy.Field unit_mly_aug = scrapy.Field unit_mly_sep = scrapy.Field unit_mly_oct = scrapy.Field unit_mly_nov = scrapy.Field unit_mly_dec = scrapy.Field'

unitMonthlyDateList = ['unit_mly_jan', 'unit_mly_feb', 'unit_mly_mar', 'unit_mly_apr', 'unit_mly_may', 'unit_mly_jun', 'unit_mly_jul', 'unit_mly_aug', 'unit_mly_sep', 'unit_mly_oct', 'unit_mly_nov', 'unit_mly_dec']


In [70]: clean_unit_mly = re.findall(r'unit\_mly\_p\_[a-z]{3}', unit_mly_p_dec)

In [71]: print clean_unit_mly
['unit_mly_p_jan', 'unit_mly_p_feb', 'unit_mly_p_mar', 'unit_mly_p_apr', 'unit_mly_p_may', 'unit_mly_p_jun', 'unit_mly_p_jul', 'unit_mly_p_aug', 'unit_mly_p_sep', 'unit_mly_p_oct', 'unit_mly_p_nov', 'unit_mly_p_dec']

#finanl list
unitMonthlyPriceList = ['unit_mly_p_jan', 'unit_mly_p_feb', 'unit_mly_p_mar', 'unit_mly_p_apr', 'unit_mly_p_may', 'unit_mly_p_jun', 
'unit_mly_p_jul', 'unit_mly_p_aug', 'unit_mly_p_sep', 'unit_mly_p_oct', 'unit_mly_p_nov', 'unit_mly_p_dec']

unit_mly_nos_jan = scrapy.Field unit_mly_nos_feb = scrapy.Field unit_mly_nos_mar = scrapy.Field unit_mly_nos_apr = scrapy.Field unit_mly_nos_may = scrapy.Field unit_mly_nos_jun = scrapy.Field unit_mly_nos_jul = scrapy.Field unit_mly_nos_aug = scrapy.Field unit_mly_nos_sep = scrapy.Field unit_mly_nos_oct = scrapy.Field unit_mly_nos_nov = scrapy.Field unit_mly_nos_dec = scrapy.Field

#unit no_of_sales_
unitMonthlyNoofsalesList = ['unit_mly_nos_jan', 'unit_mly_nos_feb', 'unit_mly_nos_mar', 'unit_mly_nos_apr', 'unit_mly_nos_may', 'unit_mly_nos_jun', 
'unit_mly_nos_jul', 'unit_mly_nos_aug', 'unit_mly_nos_sep', 'unit_mly_nos_oct', 'unit_mly_nos_nov', 'unit_mly_nos_dec']
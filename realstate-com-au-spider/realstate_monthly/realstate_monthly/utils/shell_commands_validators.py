response.xpath('//div[contains(@class, "slide-section median-price-subsections trend") and contains(name(), '"price"') and contains(name(),'"count"')]').extract()
unit_price_data = re.findall(r'\"unit\":\{\"\d+-\d+-\d+(?=).+true\}\}\,', data_center)
house_price_data = re.findall(r'\"house\":\{\"\d+-\d+-\d+(?=).+true\}\}\}\}', datacenter)


unit_monthly_data = re.findall('\"2015\-\d+\-\d+\"\:\{\"price\"\:\d.+\,\"count\"\:\d+', str(unit_price_data))
unit_yearly_data = re.findall('\"20[0-9]{1}[^5]\-\d+\-\d+\"\:\{\"price\"\:\d+.\d+\,\"count\"\:\d+\}', str(unit_price_data))

house_monthly_data = re.findall('"2015\-\d+\-\d+\"\:\{\"price\"\:\d.+\,\"count\"\:\d+', str(house_price_data))
house_yearly_data = re.findall('\"20[0-9]{1}[^5]\-\d+\-\d+\"\:\{\"price\"\:\d+.\d+\,\"count\"\:\d+\}', str(house_price_data))

#unit_monthly_data
['"2015-01-31":{"price":485000,"count":9},"2015-02-28":{"price":498000,"count":9},
"2015-03-31":{"price":482000,"count":10},"2015-04-30":{"price":452500,"count":14},
"2015-05-31":{"price":450000,"count":15},"2015-06-30":{"price":422500,"count":16},
"2015-07-31":{"price":390000,"count":13},"2015-08-31":{"price":392500,"count":14},
"2015-09-30":{"price":392500,"count":14},"2015-10-31":{"price":395000,"count":13},
"2015-11-30":{"price":395000,"count":13},"2015-12-21":{"price":395000.0,"count":13']

unit_monthly_date = re.findall(r'2015\-\d+\-\d+',str(unit_monthly_data))
unit_monthly_price = re.findall(r'[0-9]{6}',str(unit_monthly_data))
unit_monthly_no_of_sales = re.findall(r'\"count\":\d+',str(unit_monthly_data))
replaced_unit_monthly_no_of_sales = str(unit_monthly_no_of_sales).replace('"count":', '')

#unit yearly data
#['"2006-12-31":{"price":362500,"count":18}', 
#'"2007-12-31":{"price":299750,"count":27}', 
#'"2008-12-31":{"price":355000,"count":19}', 
#'"2009-12-31":{"price":367000,"count":29}', '
#"2010-12-31":{"price":407000,"count":25}', '
#"2011-12-31":{"price":520250,"count":12}', '
#"2012-12-31":{"price":370000,"count":17}', '
#"2013-12-31":{"price":420000,"count":21}', '
#"2014-12-31":{"price":475500,"count":8}']

unit_yearly_date = re.findall('\d+\-\d+\-\d+',str(unit_yearly_data))
unit_yearly_price = re.findall('[0-9]{6}',str(unit_yearly_data))
unit_yearly_no_of_sales = re.findall('\"count\":\d+',str(unit_yearly_data))
replaced_unit_yearly_no_of_sales = str(unit_yearly_no_of_sales).replace('"count":', '')
#house_monthly_data
#'"2015-01-31":{"price":765000,"count":49},
#"2015-02-28":{"price":794000,"count":48},
#"2015-03-31":{"price":775000,"count":44},
#"2015-04-30":{"price":767500,"count":38},
#"2015-05-31":{"price":800000,"count":42},
#"2015-06-30":{"price":815000,"count":38},
#"2015-07-31":{"price":815000,"count":38},
#"2015-08-31":{"price":815000,"count":40},
#"2015-09-30":{"price":800000,"count":39},
#"2015-10-31":{"price":780000,"count":39},
#"2015-11-30":{"price":790000,"count":34},
#"2015-12-21":{"price":790000.0,"count":34'

house_monthly_date = re.findall(r'2015\-\d+\-\d+',str(house_monthly_data))
house_monthly_price = re.findall(r'[0-9]{6}',str(house_monthly_data))
house_monthly_no_of_sales = re.findall(r'\"count\":\d+',str(house_monthly_data))
replaced_house_monthly_no_of_sales = str(house_monthly_no_of_sales).replace('"count":', '')
#house yearly data[
#'"2006-12-31":{"price":680000,"count":37}', 
#'"2007-12-31":{"price":777500,"count":32}', 
#'"2008-12-31":{"price":535000,"count":19}', 
#'"2009-12-31":{"price":460000,"count":40}', 
#'"2010-12-31":{"price":680000,"count":40}', 
#'"2011-12-31":{"price":702000,"count":29}', 
#'"2012-12-31":{"price":712500,"count":44}',
# '"2013-12-31":{"price":720000,"count":69}', 
#'"2014-12-31":{"price":770000,"count":50}']
#
house_yearly_date = re.findall('\d+\-\d+\-\d+',str(house_yearly_data))
house_yearly_price = re.findall('[0-9]{6}',str(house_yearly_data))
house_yearly_no_of_sales = re.findall('\"count\":\d+',str(house_yearly_data))
replaced_house_yearly_no_of_sales = str(house_yearly_no_of_sales).replace('"count":', '')

def getListOfPhotos(self, hxs, newItem):

        vPicList= ['LM_Photo_1', 'LM_Photo_2', 'LM_Photo_3', 'LM_Photo_4', 'LM_Photo_5', 'LM_Photo_6', 'LM_Photo_7', 'LM_Photo_8',
                    'LM_Photo_9', 'LM_Photo_10']

        for x in vPicList:
            newItem[x] = ''

        index=0

        for x in hxs.xpath("//div[@class=\'carousel-inner\']/div/a/img/@data-original").extract():
        
            newItem[vPicList[index]] = x
            index=index+1

            if index>9:
                break
!#/
 [unit_mly_jan, unit_mly_feb, unit_mly_mar, unit_mly_apr, unit_mly_may, unit_mly_jun, unit_mly_jul, unit_mly_aug, unit_mly_sep, unit_mly_oct, unit_mly_nov, unit_mly_dec]
 unit_mly_jan = scrapy.Field() unit_mly_feb = scrapy.Field() unit_mly_mar = scrapy.Field() unit_mly_apr = scrapy.Field() unit_mly_may = scrapy.Field() unit_mly_jun = scrapy.Field() unit_mly_jul = scrapy.Field() unit_mly_aug = scrapy.Field() unit_mly_sep = scrapy.Field() unit_mly_oct = scrapy.Field() unit_mly_nov = scrapy.Field() unit_mly_dec = scrapy.Field() #unit_monthly_avg_price unit_mly_p_jan = scrapy.Field() unit_mly_p_feb = scrapy.Field() unit_mly_p_mar = scrapy.Field() unit_mly_p_apr = scrapy.Field() unit_mly_p_may = scrapy.Field() unit_mly_p_jun = scrapy.Field() unit_mly_p_jul = scrapy.Field() unit_mly_p_aug = scrapy.Field() unit_mly_p_sep = scrapy.Field() unit_mly_p_oct = scrapy.Field() unit_mly_p_nov = scrapy.Field() unit_mly_p_dec = scrapy.Field() #unit_monthly_no_of_sales unit_mly_nos_jan = scrapy.Field() unit_mly_nos_feb = scrapy.Field() unit_mly_nos_mar = scrapy.Field() unit_mly_nos_apr = scrapy.Field() unit_mly_nos_may = scrapy.Field() unit_mly_nos_jun = scrapy.Field() unit_mly_nos_jul = scrapy.Field() unit_mly_nos_aug = scrapy.Field() unit_mly_nos_sep = scrapy.Field() unit_mly_nos_oct = scrapy.Field() unit_mly_nos_nov = scrapy.Field() unit_mly_nos_dec = scrapy.Field()
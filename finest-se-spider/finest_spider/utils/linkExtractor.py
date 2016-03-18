
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
import sys
from bs4 import BeautifulSoup
from scrapy.selector import HtmlXPathSelector
import re 

class DmozSpider(BaseSpider):
    name = "page2_actor_movie_mlink"
    allowed_domains = ["hindilinks4u.net"]

    f = open("page1_actors_n_links") 
    start_urls = re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+', str(f.read())) 
    f.close() 

    def parse(self, response):
        start = response.url.find("=")
        actor_name = response.url[start+1:]
        actor_link = str(response.url)

        sel = Selector(response)
        actor_movie_mlink  = sel.xpath("/html/body/div/div[6]/ul/li").extract()
        actor_movie_mlink = str(actor_movie_mlink).strip('[]')
        soup = BeautifulSoup(actor_movie_mlink)
        movie_name_link = soup.find_all("a")
        
        for l in movie_name_link:
            movie_link = l.get("href")
            movie_name = l.get_text()
            
            
            f = open("pag2_actor_movie_mlink","a+")
            print >>f, ", ".join([actor_name, actor_link, movie_name, movie_link])
            print [actor_name, actor_link, movie_name, movie_link]
            f.close()
           
        

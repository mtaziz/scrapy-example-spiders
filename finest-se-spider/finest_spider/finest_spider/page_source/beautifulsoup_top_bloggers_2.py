from bs4 import BeautifulSoup


def extract_urls(path):
    try:
        with open(path) as html_file:
            soup = BeautifulSoup(html_file.read()).find_all('h2', class_="undln_tit")
            # print (soup)
            items = []
            print (len(soup))
            count = len(soup)
            # for i in xrange(1, count)
            for i in xrange(1, (count+1)):
                for div in soup:
                # links = div.findAll('a')
                # for a in links:
                    urls = div.find('a').get('href')
                    items.append(urls)
                i += 1

                # with open('soup_test_div_class.txt', 'w') as file_open:
            #     file_open(str(soup))
            # return [link.get('href') for link in BeautifulSoup(html_file.read()).find_all('a')]
                return items
            print (items)
                # return [link.get('href') for link in links]
            # items = str(items)
    except IOError:
        return []


def main():
    result = extract_urls('page_source_top_bloggers_2.html')
    with open('urls_top_bloggers_2.csv', 'w') as f:
        f.write(str(result))
    f.close()

if __name__ == '__main__':
    main()

# table = soup.find('table', {'class': 'tableFile2'})
# rows = table.findAll('tr')
# for tr in rows:
#     cols = tr.findAll('td')
#     if len(cols) >= 4 and "2013" in cols[3].text:
#         link = cols[1].find('a').get('href')
#         print link
#  blog_link.xpath('.//div[@class="ser_desc"]/@href')
#  div = soup.find('div', class_="crBlock ")
# #  
# <div class="ser_desc">
# <h1> <a href="http://finest.se/annicaenglund">Annica Englund</a></h1>
#  title = post.find('h2').text.strip()
#     url = post.find('h2').a.get('href')
#     
#     for t in xrange(temp,(count+1)):
    # state.append('tripura')
# temp = t+1 
# 
# <h2 class="undln_tit">
#                                                     <a href="http://finest.se/jsfnlndqvst">
#                                                         <div class="lim-cnt">josefinmarialundquist</div>                                                    </a>
#                                                 </h2>

# <h2 class="undln_tit">
#                                                     <a href="http://finest.se/jsfnlndqvst">
#                                                         <div class="lim-cnt">josefinmarialundquist</div>                                                    </a>
#                                                 </h2>
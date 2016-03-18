from bs4 import BeautifulSoup
import pickle
import codecs

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
                # process_urls = div.find()
                    urls = div.find('a').get('href')
                    
                    # for row in tabulka.findAll('tr'):
                    # col = row.findAll('td')
                    # prvy = col[0].string.strip()
                    # druhy = col[1].string.strip()
                    # record = '%s;%s' % (prvy, druhy) # store the record with a ';' between prvy and druhy
                    # records.append(record)
                    # urls = str(urls)
                    # urls = ''.join(div.find('a').get('href'))
                    # encode('ascii', 'ignore').decode('ascii')
                    # for row in get_rows:
                    #     text = ''.join(row.findAll(text=True))
                    #     data = text.strip()
                    #     print data
                    # urls.string.encode("UTF-8")
                    #to generate a list of urls####
                    # items.append(urls)
                    ##to generate links in new line
                    items.append(str(urls))
                i += 1

                # with open('soup_test_div_class.txt', 'w') as file_open:
            #     file_open(str(soup))
            # return [link.get('href') for link in BeautifulSoup(html_file.read()).find_all('a')]
                return items
            # print (items)
                # return [link.get('href') for link in links]
            # items = str(items)
    except IOError:
        return []


def main():
    result = extract_urls('page_source_general_blogger_3.html')
    # import io
    # f = io.open('urls_general_blogger_3_split_1.csv', 'w', encoding='utf8')
    f = codecs.open('urls_general_blogger_3_split_1.txt', 'wb', 'utf8')
    # with open('urls_general_blogger_3_split_1.txt', 'wb') as f:
        # f.write(result.encode('utf8') + '\n')
        # fl = codecs.open('output.txt', 'wb', 'utf8')
    line = ';'.join(result)
    f.write(line + u'\r\n')
        #     fl.close()

    # for item in result:
        # f.write("%s\n" % item)
        #links as a list
        #pickle.dump(itemlist, outfile)
        # pickle.dump(result, f)
        # f.write(str(result))
        ## as new lines for each link
        # f.write("\n".join(result.encode('ascii', 'ignore').decode('ascii','ignore')))
        # decode('ascii', 'ignore')
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
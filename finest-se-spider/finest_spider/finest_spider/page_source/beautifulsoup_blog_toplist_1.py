from bs4 import BeautifulSoup


def extract_urls(path):
    try:
        with open(path) as html_file:
            data = BeautifulSoup(html_file.read())
            soup = data.find_all('div', class_="ser_desc")
            # print (soup)
            # soup.strip()
            items = []
            print (len(soup))
            count = len(soup)
            # for i in xrange(1, count)
            for i in xrange(1, (count+1)):
                for div in soup:
                # links = div.findAll('a')
                # for a in links:
                    urls = div.find('h1').a.get('href')
                    # div.string = urls 
                    items.append(str(urls))

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

# with open('content.html', 'w') as alllinks:
#     alllinks.write("\n".join(jobsinghana_links + modernghana_links))


def main():
    result = extract_urls('page_source_blog_toplist_1.html')
    with open('urls_blog_toplist_1_split_1.txt', 'w') as f:
        f.write("\n".join(result))
        # f.write(str(result))
        # f.write("\n")
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
# row = row.text
                # row = row.split('\n')
                # row = str(row)
#  x = soup.find_all('div',class_='info') #for book for tag in x:
#             info = tag.getText().encode('utf-8')
#             s = [line.strip() for line in info.split('\n') if len(line.strip()) > 2]
#             s.append(tag.a['href'])
#             info = '\t'.join(s)
#             print info
# def jobsinghana():
#     site = "http://www.jobsinghana.com/jobs"
#     hdr = {'User-Agent' : 'Mozilla/5.0'}
#     req = urllib2.Request(site, headers=hdr)
#     mayday = urllib2.urlopen(req)
#     soup = BeautifulSoup(mayday)
#     return map(str, soup.find_all('a', {'class' : 'hover'}))


# def modernghana():
#     site = "http://www.modernghana.com/GhanaHome/classifieds/list_classifieds.asp?    menu_id=7&sub_menu_id=362&gender=&cat_id=173&has_price=2"
#     hdr = {'User-Agent' : 'Mozilla/5.0'}
#     req = urllib2.Request(site, headers=hdr)
#     jobpass = urllib2.urlopen(req)
#     soup = BeautifulSoup(jobpass)
#     jobs = soup.find_all('a', href = re.compile('show_classifieds'))
#     result = []
#     for a in jobs:
#         header = a.parent.find_previous_sibling('h3').text
#         a.string = header
#         result.append(str(a))
#     return result

# jobsinghana_links = jobsinghana()
# modernghana_links = modernghana()


# with open('content.html', 'w') as alllinks:
#     alllinks.write("\n".join(jobsinghana_links + modernghana_links))


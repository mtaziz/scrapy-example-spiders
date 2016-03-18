from selenium import webdriver
from scrapy.http import HtmlResponse
import time 
import os
import random
from scrapy.conf import settings
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.downloadermiddlewares.retry import RetryMiddleware
# from scrapy import log
# from scrapy.conf import settings


class RetryChangeProxyMiddleware(RetryMiddleware):
    '''
    use tor and polipo to change proxy
    '''

    def _retry(self, request, reason, spider):
        # log.msg('Changing proxy')
        request.meta['proxy'] = settings.get('HTTP_PROXY')
        return RetryMiddleware._retry(self, request, reason, spider)


class ProxyMiddleware(object):
    ''' just for testing
    '''

    def process_request(self, request, spider):
        request.meta['proxy'] = settings.get('HTTP_PROXY')

# class PhantomjsMiddleware(object):
#     def process_request(self, request, spider):
#         driver = webdriver.PhantomJS()
#         driver.get('https://www.angel.co/companies')
#         # more_button = driver.find_element_by_xpath('//*[@class="more"]')
#         # more_button = driver.find_element_by_xpath('//body').get_attribute("MORE")
#         # more_button = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "more")]'))).click()
#         # driver.find_element_by_xpath('//body').get_attribute("innerHTML")
#         # //*[@id="root"]/div[4]/div[2]/div/div[2]/div[2]/div[2]/div[22]
#         # html.notranslate.scheme-light_gray_backdrop.ml.no-ms.no-mm.size-extra-large.responsive.js.no-touch.csstransforms.csstransitions.smil.no-overflowscrolling.filereader.no-force-desktop.wf-aktivgroteskstd-n2-active.wf-aktivgroteskstd-n3-active.wf-alternategothicno3d-n4-active.wf-dincondensedweb-n4-active.wf-active body.dl85.layouts.fbe11.base._a._jm div#root.dl85.layouts.ffr55.footer._a._jm div.page.unmodified.dl85.layouts.fhr17.header._a._jm div.companies.dc59.fix36._a._jm div.main_container div.content div.dc59.frs86._a._jm div.results div.more
#         # //*[@id="root"]/div[4]/div[2]/div/div[2]/div[2]/div[2]/div[22]
#         # /html/body/div[1]/div[4]/div[2]/div/div[2]/div[2]/div[2]/div[22]
#         #         try:
#             # self.loadUrl(dummyURL)

#             # WebDriverWait(self.driver, WAIT_TIME_FOR_ELEMENT).until(EC.presence_of_element_located((By.XPATH, "//a[@class=\'btn btn-primary phone-agent-button\']")) ).click()
#             # time.sleep(SLEEP_TIME)

#             # WebDriverWait(self.driver, WAIT_TIME_FOR_ELEMENT).until(EC.presence_of_element_located((By.ID, "RequestPhoneForm_email")) )
#             # self.driver.execute_script(' document.getElementById("RequestPhoneForm_email").value="dhthummala@gmail.com"; document.getElementById("RequestPhoneForm_acceptemailoffers").checked=true; ')
#             # WebDriverWait(self.driver, WAIT_TIME_FOR_ELEMENT).until(EC.presence_of_element_located((By.XPATH, "//form[@id=\'form-request-phone\']/fieldset/button")) ).click()        
#         # more_button.click()
#         time.sleep(5)
#         body = driver.page_source
#         return HtmlResponse(driver.current_url, body=body, encoding='utf-8', request=request)


class RandomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        ua = random.choice(settings.get('USER_AGENT_LIST'))
        if ua:
            request.headers.setdefault('User-Agent', ua)


# class ProxyMiddleware(object):
#     def process_request(self, request, spider):
#         request.meta['proxy'] = settings.get('HTTP_PROXY')
# class SeleniumMiddleware(object):
#    def process_request(self, request, spider):
#        if request.url == spider.search_url and spider.name == 'dr_spider':
#            driver = webdriver.Firefox()
#            form_data = spider.form_data

#            driver.get(request.url)

#            postal_code_field = driver.find_element_by_name('filter[postal_code]')
#            radius_field = driver.find_element_by_name('filter[radius]')
#            search_button = driver.find_element_by_xpath('//*[@id="edit-submit"]')

#            postal_code_field.send_keys(form_data['postal_code'])
#            radius_field.send_keys(form_data['radius'])
#            search_button.click()

#            body = driver.page_source
#            return HtmlResponse(driver.current_url, body=body, encoding='utf-8', request=request)
#        else:
#            return None

# class JSMiddleware(object):
#    def process_request(self, request, spider):
#        driver = webdriver.PhantomJS()
#         driver.get('http://www.cppcc.gov.cn/CMS/icms/project1/cppcc/wylibary/wjWeiYuanList.jsp')


#    # select from the dropdown
#        more_btn = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, '_button_select'))
#                )
#        more_btn.click()
#        driver.find_element_by_css_selector("select#tabJcwyxt_jiebie > option[value='teyaoxgrs']").click()
#        driver.find_element_by_css_selector("select#tabJcwyxt_jieci > option[value='d11jie']").click()
#        search2 = driver.find_element_by_class_name('input_a2')
#        search2.click()
#        time.sleep(5)

#        #get the response
#        body = driver.page_source
#        return HtmlResponse(driver.current_url, body=body, encoding='utf-8', request=request)

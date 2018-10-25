# -*- coding: utf-8 -*-

import platform
import logging
import time

from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

logging.basicConfig(level=logging.INFO)

chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_argument('headless')
chrome_opt.add_argument('no-sandbox')
#prefs={"profile.managed_default_content_settings.images":2}
#chrome_opt.add_experimental_option("prefs",prefs)
sysstr = platform.system()
file = 'chromedriver.exe'
if sysstr in "Linux":
    file = 'chromedriver'
browser = webdriver.Chrome(executable_path=file,options=chrome_opt)
browser.set_page_load_timeout(40)

#入口第一页开始 打印网站大图地址
browser.get('http://jandan.net/ooxx/page-1#comments')

flag = True
while flag:
    urls = browser.find_elements_by_xpath('//div[@class="text"]/p/a')
    for url in urls:
        logging.info(url.get_attribute('href'))
    time.sleep(1)
    try:
        browser.find_element_by_class_name('next-comment-page').click()
    except NoSuchElementException as e:
        flag = False



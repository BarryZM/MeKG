#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
# 使用headless无界面浏览器模式
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 启动浏览器，获取网页源代码
browser = webdriver.Chrome(options=chrome_options)
browser.implicitly_wait(10)
mainUrl = "https://clinicaltrials.gov/ct2/show/NCT04655014?draw=2&rank=6"
browser.get(mainUrl)
# WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//a[@id="rowId100"]')))

result = {}
table = browser.find_elements_by_xpath('//div[@class="tr-subsection"]')
for i in table:
    topic = i.find_element_by_xpath('./div[@class="ct-header2"]')
    if topic.text.strip() == 'Study Description':
        content = i.find_element_by_xpath('../div[@class="tr-indent2"]')
        result['StudyDescription'] = content.text
    if topic.text.strip() == 'Study Design':
        content = i.find_element_by_xpath('../table')
        result['StudyDesign'] = content.text
    if topic.text.strip() == 'Arms and Interventions':
        content = i.find_element_by_xpath('../div/table[contains(@class,"ct-data_table")]')
        result['ArmsandInterventions'] = content.text
    if topic.text.strip() == 'Outcome Measures':
        content = i.find_element_by_xpath('../div[@class="tr-indent3"]')
        result['OutcomeMeasures'] = content.text
    if topic.text.strip() == 'Groups and Cohorts':
        content = i.find_element_by_xpath('../div[@class="tr-indent3"]')
        result['GroupsandCohorts'] = content.text
    if topic.text.strip() == 'Eligibility Criteria':
        content = i.find_element_by_xpath('../div[@class="tr-indent2"]')
        result['EligibilityCriteria'] = content.text
    if topic.text.strip() == 'Contacts and Locations':
        content = i.find_element_by_xpath('../div[@class="tr-indent2"]')
        result['ContactsandLocaons'] = content.text
    if topic.text.strip() == 'More Information':
        content = i.find_element_by_xpath('../div[@class="tr-indent2"]')
        result['MoreInformation'] = content.text

browser.quit()
print(result)

from selenium import webdriver
import os


class ScrapyMe(object):
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        # 使用headless无界面浏览器模式
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')

        # 启动浏览器，获取网页源代码
        self.browser = webdriver.Chrome(options=chrome_options)
        self.browser.implicitly_wait(10)

    def scrapy_mess(self, url):
        self.browser.get(url)
        result = {}
        table = self.browser.find_elements_by_xpath('//div[@class="tr-subsection"]')
        for i in table:
            topic = i.find_element_by_xpath('./div[@class="ct-header2"]')
            try:
                if topic.text.strip() == 'Study Description':
                    content = i.find_element_by_xpath('../div[@class="tr-indent2"]')
                    result['studyDescription'] = content.text
            except Exception as err:
                with open('error.txt', 'a') as f:
                    f.write(f'error: {err},url:{url}-------- Study Description')
                print(f'error: {err},url:{url} -------- Study Description')

            try:
                if topic.text.strip() == 'Study Design':
                    content = i.find_element_by_xpath('../table')
                    result['studyDesign'] = content.text
            except Exception as err:
                with open('error.txt', 'a') as f:
                    f.write(f'error: {err},url:{url}-------- Study Design')
                print(f'error: {err},url:{url} -------- Study Design')

            try:
                if topic.text.strip() == 'Arms and Interventions':
                    content = i.find_element_by_xpath('../div/table[contains(@class,"ct-data_table")]')
                    result['armsandInterventions'] = content.text
            except Exception as err:
                with open('error.txt', 'a') as f:
                    f.write(f'error: {err},url:{url}-------- Arms and Interventions')
                print(f'error: {err},url:{url} --------Arms and Interventions')

            try:
                if topic.text.strip() == 'Outcome Measures':
                    content = i.find_element_by_xpath('../div[@class="tr-indent3"]')
                    result['outcomeMeasures'] = content.text
            except Exception as err:
                with open('error.txt', 'a') as f:
                    f.write(f'error: {err},url:{url}-------- Outcome Measures')
                print(f'error: {err},url:{url} --------Outcome Measures')

            try:
                if topic.text.strip() == 'Groups and Cohorts':
                    content = i.find_element_by_xpath('../div[@class="tr-indent3"]')
                    result['groupsandCohorts'] = content.text
            except Exception as err:
                with open('error.txt', 'a') as f:
                    f.write(f'error: {err},url:{url}-------- Groups and Cohorts')
                print(f'error: {err},url:{url} --------Groups and Cohorts')

            try:
                if topic.text.strip() == 'Eligibility Criteria':
                    content = i.find_element_by_xpath('../div[@class="tr-indent2"]')
                    result['eligibilityCriteria'] = content.text
            except Exception as err:
                with open('error.txt', 'a') as f:
                    f.write(f'error: {err},url:{url}-------- Eligibility Criteria')
                print(f'error: {err},url:{url} --------Eligibility Criteria')

            try:
                if topic.text.strip() == 'Contacts and Locations':
                    content = i.find_element_by_xpath('../div[@class="tr-indent2"]')
                    result['contactsandLocaons'] = content.text
            except Exception as err:
                with open('error.txt', 'a') as f:
                    f.write(f'error: {err},url:{url}-------- Contacts and Locations')
                print(f'error: {err},url:{url} --------Contacts and Locations')

            try:
                if topic.text.strip() == 'More Information':
                    content = i.find_element_by_xpath('../div[@class="tr-indent2"]')
                    result['moreInformation'] = content.text
            except Exception as err:
                with open('error.txt', 'a') as f:
                    f.write(f'error: {err},url:{url}-------- More Information')
                print(f'error: {err},url:{url} --------More Information')
        return result

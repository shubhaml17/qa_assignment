import time

from selenium.webdriver.common.by import By

from Utility.common_utility import get_web_driver


class WikiPage:

    def __init__(self, driver):
        self.driver = driver

    def get_list_of_language_table(self):
        language = []
        lists_of_language = self.driver.find_elements(By.XPATH, "//tbody/tr/td[2]/a")
        time.sleep(2)
        for l in lists_of_language:
            language.append(l.text)
        return language

    def get_articles_list(self):
        article = []
        list_of_article = self.driver.find_elements(By.XPATH, "//tbody//tr/td[5]/a/b")

        for articles in list_of_article:
            article.append(articles.text)
        return article

    def find_article_by_language(self):
        languages = self.get_list_of_language_table()
        articles = self.get_articles_list()
        d = dict(zip(languages, articles))
        return d

    def total_sum_article_languages(self, langauages):

        sum = 0
        d = self.find_article_by_language()
        for k, v in d.items():
            if k in langauages:
                print(f"language is {k} and  value is {v}")
                sum += int(v.replace(',', ''))
        return sum

    def find_total_articles_by_languages(self, language):

        articles = []
        rows = self.driver.find_elements(By.XPATH, "//tbody//tr")

        for r in rows:
            get_language = r.find_element(By.XPATH, ".//td[2]/a")
            if get_language.text in language:
                print(get_language.text)
                article = r.find_element(By.XPATH, ".//td[5]//a//b")
                articles.append(article.text)
                if len(language) == len(articles):
                    break

        sum = 0
        for s in articles:
            sum += int(s.replace(',', ''))
        print(f"Total sum is: {sum}")
        return sum


driver = get_web_driver("https://meta.wikimedia.org/wiki/List_of_Wikipedias/Table")

wiki_page = WikiPage(driver)

wiki_page.find_total_articles_by_languages(['English', 'German'])

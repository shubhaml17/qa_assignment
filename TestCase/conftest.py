from Utility.common_utility import get_web_driver
import pytest
from Page.wiki_page import WikiPage

WIKI_PAGE_LINK = "https://meta.wikimedia.org/wiki/List_of_Wikipedias/Table"


@pytest.fixture(scope='class')
def launch_wiki_page(request):
    driver = get_web_driver(WIKI_PAGE_LINK)
    wiki_page = WikiPage(driver)
    request.cls.driver = driver
    request.cls.wiki_page = wiki_page
    yield
    driver.close()

import pytest

from Page.wiki_page import WikiPage


@pytest.mark.usefixtures('launch_wiki_page')
class TestWikiPageArticleValue:

    @pytest.mark.parametrize('langauge', ['English', 'German', 'French'])
    def test_language(self, langauge):
        get_langauge_list = self.wiki_page.get_list_of_language_table()
        assert langauge in get_langauge_list, "Langauge not found"

    def test_validate_article_value_by_langauge(self):
        get_article_value = self.wiki_page.find_article_by_language()
        assert get_article_value['English'] == '6,562,386', "Getting Wrong value"

    def test_sum_of_article(self):
        list_of_languages = ['English', 'Swedish']
        get_sum_of_article = self.wiki_page.find_total_articles_by_languages(list_of_languages)
        actual_sum = self.wiki_page.total_sum_article_languages(list_of_languages)
        expected_sum = get_sum_of_article

        assert expected_sum == actual_sum, "Sum is incorrect"

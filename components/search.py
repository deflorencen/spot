

from playwright.sync_api import Page
from data.locators.home_locators import Home


class SearchComponent:
    def __init__(self, page: Page):
        self.page = page
        self.search_input = page.locator(Home.Search.SEARCH_INPUT)

    def type_query(self, text: str):
        self.search_input.fill(text)
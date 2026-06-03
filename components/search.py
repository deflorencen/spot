

from playwright.sync_api import Page


class SearchComponent:
    def __init__(self, page: Page):
        self.page = page
        self.search_input = page.locator('[data-testid="search-input"]')

    def type_query(self, text: str):
        self.search_input.fill(text)
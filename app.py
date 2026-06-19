from playwright.sync_api import Page

from pages.home_page import HomePage

from components.search import SearchComponent
from components.content import ContentComponent

class Application:
    def __init__(self, page: Page):
        self.page = page

        self.home_page = HomePage(page)

        self.search = SearchComponent(page)
        self.content = ContentComponent(page)

        # LOW PRIORITY
        # self.sidebar = SidebarComponent(page)


from playwright.sync_api import Page

from pages.home_page import HomePage
from pages.auth.login_page import LoginPage
from pages.auth.signup_page import SignUpPage

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

        # NOT FOR TESTING
        self.auth = AuthGroup(page)


class AuthGroup:
    def __init__(self, page: Page):
        self.login_page = LoginPage(page)
        self.sign_up_page = SignUpPage(page)
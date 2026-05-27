

class BasePage:
    URL: str | None = None

    def __init__(self, page):
        self.page = page

    def open(self, url: str = None):
        target_url = url or self.URL
        if not target_url:
            raise ValueError("URL is not defined")
        self.page.goto(target_url)

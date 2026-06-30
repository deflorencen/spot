from playwright.sync_api import Page, Locator, expect


class TopResultContent:
    def __init__(self, page: Page):
        self.page = page
        self.top_result_card = page.get_by_test_id("top-result-card")
        self.play_button = self.top_result_card.get_by_test_id("play-button")
        self.click_top_result_card = self.top_result_card.get_by_test_id("herocard-click-handler")
        self.top_result_card_image = self.top_result_card.get_by_test_id("card-image")
        self.artist_link = self.top_result_card.locator("a[href^='/artist/']")
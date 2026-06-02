

from playwright.sync_api import Page, expect
from data.locators.home_locators import Home


class ContentComponent:
    def __init__(self, page: Page):
        self.page = page

    def click_artist(self, artist_name: str):
        self.page.locator(
            Home.Content.artist_link(artist_name)
        ).click()

    def click_album(self, album_name: str):
        self.page.get_by_text(album_name, exact=True).first.click()

    def verify_album_list_visible(self, album_name: str):
        grid = self.page.get_by_text(album_name, exact=False)
        expect(grid.first).to_be_visible(timeout=5000)

    def verify_album_page_loaded(self, expected_title: str):
        title_element = self.page.locator(Home.Content.ALBUM_TITLE).first
        expect(title_element).to_have_text(expected_title, timeout=5000)

    def verify_tracks_are_visible(self, track_count: int):
        tracks = self.page.locator(Home.Content.TRACK_ROW)
        expect(tracks).to_have_count(track_count)

from playwright.sync_api import Page, Locator, expect


class ContentComponent:
    def __init__(self, page: Page):
        self.page = page

        self.album_title = page.get_by_test_id("entityTitle")
        self.track_row = page.get_by_test_id("tracklist-row")
        self.grid_container = page.get_by_test_id("grid-container")

    def artist_link(self, artist_name: str) -> Locator:
        return (
            self.page
            .get_by_test_id("top-result-card")
            .get_by_role("link", name=artist_name, exact=True)
        )

    def album_link(self, album_name: str) -> Locator:
        return (
            self.page
            .get_by_test_id("grid-container")
            # .get_by_role("link", name=album_name, exact=False)
            .locator(f'a[href^="/album/"]')
            .filter(has_text=album_name)
        )

    def open_artist(self, artist_name: str):
        self.artist_link(artist_name).click()

    def open_album(self, album_name: str):
        self.album_link(album_name).click()

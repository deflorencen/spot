

class Home:

    class Search:
        SEARCH_INPUT = '[data-testid="search-input"]'

    class Content:
        @staticmethod
        def artist_link(artist_name):
            return f'a[title="{artist_name}"]'

        @staticmethod
        def click_album(album_name):
            return f'p[title="{album_name}"]'

        ALBUM_LIST = '[data-testid="grid-container"]'

        ALBUM_TITLE = '[data-testid="entityTitle"]'
        TRACK_ROW = '[data-testid="tracklist-row"]'
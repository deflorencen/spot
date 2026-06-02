

def test_search_and_open_artist(app):
    app.home_page.open()

    app.search.type_query("Kendrick Lamar")

    app.content.click_artist("Kendrick Lamar")
    app.content.verify_album_list_visible("DAMN.")

    app.content.click_album("DAMN.")

    app.content.verify_album_page_loaded("DAMN.")
    app.content.verify_tracks_are_visible(14)
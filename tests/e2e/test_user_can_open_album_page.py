from playwright.sync_api import expect


def test_user_can_open_album_page(app):
    app.home_page.open()

    app.search.type_query("Kendrick Lamar")

    app.content.open_artist("Kendrick Lamar")
    app.content.open_album("DAMN.")

    expect(app.content.album_title).to_have_text("DAMN.")
    expect(app.content.track_row).to_have_count(14)
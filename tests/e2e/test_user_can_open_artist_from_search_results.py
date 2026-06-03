import pytest, re
from playwright.sync_api import expect

@pytest.mark.parametrize(
    "artist_name, album_name, track_count",
    [
        ("Kendrick Lamar", "DAMN.", 14),
        ("Eminem", "The Eminem Show", 20),
        ("Drake", "Views", 20),
    ]
)
def test_user_can_open_album_page(
        app,
        artist_name,
        album_name,
        track_count
):
    app.home_page.open()

    app.search.type_query(artist_name)

    app.content.open_artist(artist_name)
    app.content.open_album(album_name)

    expect(app.content.album_link(album_name)).to_have_attribute("href", re.compile(r"^/album/"))
    expect(app.content.album_title).to_have_text(album_name)
    expect(app.content.track_row).to_have_count(track_count)
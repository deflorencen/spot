import time, json

import pytest, re
from playwright.sync_api import expect


def test_user_can_open_album_page(app):
    app.home_page.open()

    app.search.type_query("Kendrick Lamar")

    app.content.open_artist("Kendrick Lamar")
    app.content.open_album("DAMN.")

    expect(app.content.album_title).to_have_text("DAMN.")
    expect(app.content.track_row).to_have_count(14)


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


def test_album_loading_server_error_handling(app):
    def handle_route(route):
        try:
            request_body = json.loads(route.request.post_data)
            operation_name = request_body.get("operationName")
        except (json.JSONDecodeError, TypeError):
            operation_name = None

        if "album" in operation_name.lower():
            route.fulfill(status=500, content_type="application/json")
        else:
            route.continue_()

    app.page.route(
        "**/pathfinder/v2/query",
        handle_route
    )

    app.home_page.open()
    app.search.type_query("Kendrick Lamar")
    app.content.open_artist("Kendrick Lamar")
    app.content.open_album("DAMN.")
    expect(app.content.track_row).to_have_count(0)


def test_top_result_content(app):
    app.home_page.open()
    app.search.type_query("Kendrick")

    expect(app.top_result_component.top_result_card).to_be_visible()
    
    expect(app.top_result_component.play_button).to_be_visible()
    expect(app.top_result_component.click_top_result_card).to_be_visible()
    expect(app.top_result_component.top_result_card_image).to_be_visible()
    expect(app.top_result_component.top_result_card_text).to_be_visible()
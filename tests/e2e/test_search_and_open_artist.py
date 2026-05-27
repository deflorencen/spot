from time import sleep


def test_search_and_open_artist(app):
    app.home_page.open()
    app.search.type_query("Ed Sheeran")
    sleep(10)


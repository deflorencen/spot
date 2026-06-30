import pytest
from pages.base_page import BasePage

def test_base_page_raises_value_error_when_url_is_missing(page):
    base_page = BasePage(page)

    with pytest.raises(ValueError) as exc_info:
        base_page.open()

    assert str(exc_info.value) == "URL is not defined"
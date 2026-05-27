import pytest
from playwright.sync_api import Page
from app import Application

@pytest.fixture(scope="function")
def app(page: Page) -> Application:
    return Application(page)
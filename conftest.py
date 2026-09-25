from playwright.sync_api import Page, expect
import pytest

from pages.login import loginPage

@pytest.fixture()
def applicationNavigation(page: Page):
    page.goto("https://www.amazon.in/")

@pytest.fixture()
def loginObj(page):
    return loginPage(page)
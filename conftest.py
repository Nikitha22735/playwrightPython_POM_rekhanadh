import allure
from playwright.sync_api import Page, expect
import pytest

from pages.login import loginPage

@pytest.fixture()
def applicationNavigation(page: Page):
    page.goto("https://www.amazon.in/")

@pytest.fixture()
def loginObj(page):
    return loginPage(page)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome= yield
    report = outcome.get_result()
    if report.when =="call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            allure.attach(page.screenshot(), name="faiulure", attachment_type=allure.attachment_type.PNG)

   
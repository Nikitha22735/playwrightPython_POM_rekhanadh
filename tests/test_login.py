from playwright.sync_api import Page, expect

from pages.home import homePage
from pages.login import loginPage

def test_positiveLogin(page: Page,applicationNavigation,loginObj):   
    homeObj = homePage(page)

    homeObj.clickOnAccountsdList()    
    loginObj.enterLoginEmail("trainingplaywright@gmail.com")
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("textbox", name="Password").fill("Welcome@04")
    page.get_by_role("button", name="Sign in").click()
    expect(page.get_by_role("searchbox", name="Search Amazon.in")).to_be_visible()


def test_negitiveLogin(page: Page,applicationNavigation):
    homeObj = homePage(page)
    loginObj = loginPage(page)
    homeObj.clickOnAccountsdList()
    loginObj.enterLoginEmail("trainingplaywright@gmail.com")
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("textbox", name="Password").dblclick()
    page.get_by_role("textbox", name="Password").fill("hhh")
    page.get_by_role("button", name="Sign in").click()
    expect(page.locator("#auth-error-message-box")).to_contain_text("Your password is incorrect")
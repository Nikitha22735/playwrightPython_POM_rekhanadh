from playwright.sync_api import Page

from pages.home import homePage


def test_positiveLogin(page: Page, applicationNavigation, loginObj):
    homeObj = homePage(page)

    homeObj.clickOnAccountsdList()
    loginObj.enterLoginEmail("trainingplaywright@gmail.com")
    loginObj.clickContinue()
    loginObj.enterLoginPassword("Welcome@04")
    loginObj.clickSignIn()
    homeObj.verifySearchBoxVisible()


def test_negativeLogin(page: Page, applicationNavigation, loginObj):
    homeObj = homePage(page)

    homeObj.clickOnAccountsdList()
    loginObj.enterLoginEmail("trainingplaywright@gmail.com")
    loginObj.clickContinue()
    loginObj.enterLoginPassword("hhh")
    loginObj.clickSignIn()
    loginObj.verifyIncorrectPasswordMessage()
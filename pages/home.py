import allure
from playwright.sync_api import expect


class homePage:
    def __init__(self, page):
        self.amazonLogoLink = page.get_by_role("link", name="Amazon.in")
        self.searchTextBox = page.get_by_role("searchbox", name="Search Amazon.in")
        self.accountsNdListBtn = page.get_by_role("link", name="Hello, sign in Account & Lists")

    @allure.step("verifyAmazonLogoVisible")
    def verifyAmazonLogoVisible(self):
        expect(self.amazonLogoLink).to_be_visible()

    @allure.step("verifySearchBoxVisible")
    def verifySearchBoxVisible(self):
        expect(self.searchTextBox).not_to_be_visible()

    @allure.step("verifyAccountAndListsVisible")
    def verifyAccountAndListsVisible(self):
        expect(self.accountsNdListBtn).to_be_visible()

    @allure.step("searchForProduct")
    def searchForProduct(self, productName):
        self.searchTextBox.fill(productName)
        self.searchTextBox.press("Enter")

    @allure.step("clickOnAccountsdList")
    def clickOnAccountsdList(self):
        self.accountsNdListBtn.click()
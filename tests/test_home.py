from playwright.sync_api import Page, expect

from pages.home import homePage


def test_homeScreen(page: Page, applicationNavigation) -> None:
	homeObj = homePage(page)

	homeObj.verifyAmazonLogoVisible()
	homeObj.verifySearchBoxVisible()
	homeObj.verifyAccountAndListsVisible()

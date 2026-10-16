from playwright.sync_api import Page, expect
import pytest

from pages.home import homePage


@pytest.mark.sample
def test_homeScreen(page: Page, applicationNavigation) -> None:
	homeObj = homePage(page)

	homeObj.verifyAmazonLogoVisible()
	homeObj.verifySearchBoxVisible()
	homeObj.verifyAccountAndListsVisible()

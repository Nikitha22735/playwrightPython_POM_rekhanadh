from playwright.sync_api import Page
import pytest

from pages.home import homePage
from pages.results import resultsPage


# @pytest.mark.sample
def test_addIphoneFromResultsToCart(page: Page, applicationNavigation) -> None:
	homeObj = homePage(page)
	resultsObj = resultsPage(page)

	homeObj.searchForProduct("iphone")
	# resultsObj.verifySponsoredIphoneVisible()
	resultsObj.addSponsoredIphoneToCart()
	resultsObj.verifyCartCount(1)

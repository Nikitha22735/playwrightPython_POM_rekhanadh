from playwright.sync_api import Page

from pages.cart import cartPage
from pages.home import homePage
from pages.results import resultsPage


def test_iphoneIsVisibleInShoppingCart(page: Page, applicationNavigation) -> None:
	homeObj = homePage(page)
	resultsObj = resultsPage(page)
	cartObj = cartPage(page)

	homeObj.searchForProduct("iphone")
	resultsObj.verifySponsoredIphoneVisible()
	resultsObj.addSponsoredIphoneToCart()
	resultsObj.verifyCartCount(1)
	resultsObj.clickOnCartIcon()
	cartObj.verifyShoppingCartPageVisible()
	cartObj.verifyIphoneVisible()
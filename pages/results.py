import re

from playwright.sync_api import expect


class resultsPage:
	def __init__(self, page):
		self.sponsoredIphoneLink = page.get_by_role(
			"link", name="Sponsored Ad - iPhone 18 Pro Max (256 GB) - Burgundy"
		)
		self.iphoneResult = page.get_by_role("listitem").filter(
			has=self.sponsoredIphoneLink
		)
		self.addToCartButton = self.iphoneResult.get_by_role("button", name="Add to cart")
		self.cartCount = page.locator("#nav-cart-count")
		self.cartLink = page.get_by_role(
			"link", name=re.compile(r"\d+ items? in cart")
		)

	def verifySponsoredIphoneVisible(self):
		expect(self.sponsoredIphoneLink).to_be_visible()

	def addSponsoredIphoneToCart(self):
		self.addToCartButton.click()

	def verifyCartCount(self, expectedCount):
		expect(self.cartCount).to_contain_text(str(expectedCount))

	def clickOnCartIcon(self):
		self.cartLink.click()

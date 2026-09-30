import re

from playwright.sync_api import expect


class cartPage:
	def __init__(self, page):
		self.shoppingCartHeading = page.get_by_role(
			"heading", name="Shopping Cart", exact=True
		)
		self.iphoneProductHeading = page.get_by_role("list", name="Shopping Cart").get_by_role(
			"heading", name=re.compile(r"iPhone 18 Pro Max \(256 GB\) - Burgundy")
		)

	def verifyShoppingCartPageVisible(self):
		expect(self.shoppingCartHeading).to_be_visible()

	def verifyIphoneVisible(self):
		expect(self.iphoneProductHeading).to_be_visible()
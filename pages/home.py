class homePage:
    def __init__(self, page):
       self.accountsNdListBtn =  page.get_by_role("link", name="Hello, sign in Account & Lists")


    def clickOnAccountsdList(self):
        self.accountsNdListBtn.click()
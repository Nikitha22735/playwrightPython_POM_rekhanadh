class loginPage:
    def __init__(self, page):
       self.loginTextBx =  page.get_by_role("textbox", name="Enter mobile number or email")


    def enterLoginEmail(self,email):
        self.loginTextBx.fill(email)
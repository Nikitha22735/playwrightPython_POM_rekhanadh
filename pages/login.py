from playwright.sync_api import expect


class loginPage:
    def __init__(self, page):
        self.loginTextBx = page.get_by_role("textbox", name="Enter mobile number or email")
        self.continueBtn = page.get_by_role("button", name="Continue")
        self.passwordTextBx = page.get_by_role("textbox", name="Password")
        self.signInBtn = page.get_by_role("button", name="Sign in")
        self.authErrorMessage = page.locator("#auth-error-message-box")

    def enterLoginEmail(self, email):
        self.loginTextBx.fill(email)

    def clickContinue(self):
        self.continueBtn.click()

    def enterLoginPassword(self, password):
        self.passwordTextBx.fill(password)

    def clickSignIn(self):
        self.signInBtn.click()

    def verifyIncorrectPasswordMessage(self):
        expect(self.authErrorMessage).to_contain_text("Your password is incorrect")
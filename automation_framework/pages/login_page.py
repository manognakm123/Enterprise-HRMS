class LoginPage:
    def __init__(self, page):
        self.page = page

        self.username = "#username"
        self.password = "#password"
        self.login_button = "#login-btn"

    def open_application(self):
        self.page.goto("http://127.0.0.1:5000/login")

    def enter_username(self, username):
        self.page.fill(self.username, username)

    def enter_password(self, password):
        self.page.fill(self.password, password)

    def click_login(self):
        self.page.click("#login-btn")

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
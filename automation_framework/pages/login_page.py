from config.config import Config
from utilities.logger import get_logger


logger = get_logger()

class LoginPage:

    # logger = get_logger()

    def __init__(self, page):
        self.page = page

        self.username = "#username"
        self.password = "#password"
        self.login_button = "#login-btn"

    def open_application(self):
        self.page.goto(Config.BASE_URL + "/login")

        logger.info("Opened HRMS Login page")


    def enter_username(self, username):
        self.page.fill(self.username, username)

        logger.info("Entered Username")

    def enter_password(self, password):
        self.page.fill(self.password, password)

        logger.info("Entered Password")


    def click_login(self):
        self.page.click("#login-btn")

        logger.info("Clicked Login Button")


    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

        logger.info("Login successful")
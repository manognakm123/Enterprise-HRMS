from utilities.logger import get_logger


logger = get_logger()

class DashboardPage:

    def __init__(self, page):
        self.page = page

        self.employee_management = "text=Employee Management"


    def click_employee_management(self):
        self.page.click(self.employee_management)

        logger.info("Clicked Employee Management")


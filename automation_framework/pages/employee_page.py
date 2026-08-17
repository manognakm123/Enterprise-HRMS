from playwright.sync_api import expect
from utilities.logger import get_logger


logger = get_logger()

class EmployeePage:

    def __init__(self, page):

        self.page = page

        self.search_box = "#search"
        self.search_button = "#search-btn"

    def search_employee(self, employee_id):

        self.page.wait_for_selector(self.search_box)

        self.page.fill(self.search_box, employee_id)

        self.page.click(self.search_button)

        logger.info(f"Searching Employee {employee_id}")

    def verify_employee_presence(self, employee_id):

        expect(
            self.page.get_by_role(
                "cell",
                name=employee_id,
                exact=True
            )
        ).to_be_visible()

        
        
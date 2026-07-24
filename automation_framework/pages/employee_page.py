from playwright.sync_api import expect

class EmployeePage:

    def __init__(self, page):

        self.page = page

        self.search_box = "#search"
        self.search_button = "#search-btn"

    def search_employee(self, employee_id):

        self.page.fill(self.search_box, employee_id)

        self.page.click(self.search_button)

    def verify_employee_presence(self, employee_id):

        expect(
            self.page.locator(f"text={employee_id}")
        ).to_be_visible()
        
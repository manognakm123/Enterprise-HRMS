from playwright.sync_api import Page, expect


class AddEmployeePage:

    def __init__(self, page):

        self.page = page

        self.add_employee_button = "text=Add Employee"

        self.employee_id = "#employee_id"
        self.first_name = "#first_name"
        self.last_name = "#last_name"
        self.email = "#email"
        self.department = "#department"
        self.designation = "#designation"

        self.save_button = "#save-btn"
        
    def click_add_employee(self):
        
        self.page.click(self.add_employee_button)
    
    def add_employee(
        self,
        employee_id,
        first_name,
        last_name,
        email,
        department,
        designation
    ):
        
        self.page.fill(self.employee_id, employee_id)
        self.page.fill(self.first_name, first_name)
        self.page.fill(self.last_name, last_name)
        self.page.fill(self.email, email)
        self.page.select_option(self.department, department)
        self.page.select_option(self.designation, designation)

        self.page.click(self.save_button)


    def verify_employee_added(self, employee_id):

        expect(
            self.page.locator(f"text={employee_id}")
        ).to_be_visible()
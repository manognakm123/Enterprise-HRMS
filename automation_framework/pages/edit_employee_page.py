class EditEmployeePage:


    def __init__(self, page):

        self.page = page

        self.edit_button = "a[href='/edit_employee/EMP001']"

        self.first_name = "#first_name"

        self.last_name = "#last_name"

        self.email = "#email"

        self.department = "#department"

        self.designation = "#designation"

        self.update_button = "button[type='submit']"


    def click_edit(self):

        self.page.click(self.edit_button)


    def edit_employee(
            self,
            first_name,
            last_name,
            email,
            department,
            designation
    ):
        
        self.page.fill(self.first_name, first_name)

        self.page.fill(self.last_name, last_name)

        self.page.fill(self.email, email)

        self.page.select_option(self.department, department)

        self.page.select_option(self.designation, designation)


    def click_update(self):
        self.page.click(self.update_button)

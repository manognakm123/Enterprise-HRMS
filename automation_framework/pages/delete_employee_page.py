class DeleteEmployeePage:

    def __init__(self, page):
        self.page = page

    
    def click_delete(self, employee_id):
        
        # Accept the briwser confirmation dialog
        self.page.on(
            "dialog",
            lambda dialog: dialog.accept()
        )


        self.page.click(
            f"a[href='/delete_employee/{employee_id}']"
        )


        # # Accept the briwser confirmation dialog
        # self.page.on(
        #     "dialog",
        #     lambda dialog: dialog.accept()
        # )
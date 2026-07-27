def assert_dashboard(page):
    assert "dashboard" in page.url.lower()


def assert_login(page):
    assert "login" in page.url.lower()



def assert_employee_deleted(page, employee_id):
    assert employee_id not in page.content()



def assert_employee_exists(page, employee_id):
    assert employee_id in page.content()
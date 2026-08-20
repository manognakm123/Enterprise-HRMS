import os

class Config:

    BASE_URL = os.getenv("HRMS_BASE_URL", "http://127.0.0.1:5000")

    USERNAME = os.getenv("HRMS_USERNAME", "admin")

    PASSWORD = os.getenv("HRMS_PASSWORD", "admin123")

    BROWSER = os.getenv("BROWSER", "chromium")

    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"

    TIMEOUT = int(os.getenv("TIMEOUT", "30000"))

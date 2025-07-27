# 🚀 Travel Website Automation Framework

Automate your end-to-end testing for the BlazeDemo travel website with a modern, maintainable, and fully-configurable Python framework! Featuring Selenium, Pytest, Allure, and a robust Page Object Model (POM) structure, this project is ready for both local and CI/CD execution.

---

## ✨ Features
- **Selenium WebDriver** automation for Chrome
- **Pytest** for modular, scalable test structure
- **Allure** for beautiful, interactive test reports (with screenshots on failure)
- **Page Object Model (POM)** for clean, maintainable code
- **Configurable** via `config.ini` (URLs, credentials, negative test data, etc.)
- **GitHub Actions** pipeline for CI/CD
- **Automatic screenshots** on test failure: Instantly debug with images saved in the `Screenshots/` folder
- **Easy test data management**: All login and registration test data is externalized in `config.ini`

---

## 🗂️ Project Structure
```
├── Configurations/
│   └── config.ini           # All environment/test data (usernames, passwords, negative cases, etc.)
├── Pages/
│   ├── LoginPage.py         # POM for Login
│   ├── RegisterPage.py      # POM for Register
│   └── FlightBookingPage.py # POM for Booking
├── Testcases/
│   ├── test_Login.py        # Login test scenarios (all data from config.ini)
│   ├── test_Register.py     # Registration test scenarios (all data from config.ini)
│   ├── test_FlightBooking.py# Booking test scenarios
│   ├── conftest.py          # Pytest fixtures & hooks (auto-screenshot on failure)
│   └── Screenshots/         # Screenshots on failure
├── Utilities/
│   ├── ReadProperties.py    # Config reader (all test data access)
│   └── Email.py             # Email automation for report sharing
├── requirements.txt         # Python dependencies
├── Jenkinsfile              # (Optional) Jenkins pipeline
├── .github/workflows/main.yml # GitHub Actions pipeline
└── README.md                # This file
```

---

## ⚡ Quickstart

1. **Clone the repo:**
   ```sh
   git clone <your-repo-url>
   cd TravelWebsiteAutomation-main
   ```
2. **Create & activate a virtual environment:**
   ```sh
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On Linux/Mac:
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run tests and generate Allure report:**
   ```sh
   pytest --alluredir=Reports
   allure generate --single-file Reports\index.html --clean
   ```
   - The Allure HTML report will be available at `Reports/index.html`.

---

## 🧪 Example Test Scenarios
- Valid and invalid login (wrong password, blank fields, invalid email, all from config.ini)
- Registration with valid/invalid data (blank fields, mismatched passwords, invalid email, existing user)
- Flight booking flow
- UI element checks
- Screenshots on failure (auto-attached to Allure report)

---

## 🤖 CI/CD with GitHub Actions
- Tests run automatically on every push or PR to `main`
- Allure results are uploaded as an artifact
- Chrome and ChromeDriver are installed in the pipeline
- Virtual environment and dependencies are managed in the workflow

---

## 📸 Screenshots on Failure
If a test fails, a screenshot is saved in `Screenshots/FAIL_<testname>.png` and attached to the Allure report for instant debugging.

---

## 🛠️ Tech Stack
- Python 3.11+
- Selenium
- Pytest
- Allure
- GitHub Actions
- Page Object Model (POM)

---

## 💡 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

If you want to contribute to this framework, let's work together and make it even better! 🚀

If you have amazing ideas for automation, or want to collaborate on new features, let's connect!

---

## 🧩 Data-Driven & Configurable

This framework is fully **data-driven**. All test data—including valid, negative, edge, and special cases—is managed in a single, easy-to-edit `config.ini` file under `Configurations/`.

- **How it works:**
  - Test data for registration, login, and booking is never hardcoded. Instead, it is read at runtime from `config.ini` using utility methods in `Utilities/ReadProperties.py`.
  - The framework uses Python’s `configparser` (with interpolation disabled) to safely parse all values, including those with special characters, unicode, or symbols.
  - To add or update test scenarios, simply edit `config.ini`—no code changes required!

**Example config entry:**
```ini
[REGISTER]
valid_email = validuser@example.com
weak_password = 12345
symbols_password = !@#$%^&*()
```

**How to access in tests:**
```python
from Utilities.ReadProperties import ReadConfig
email = ReadConfig.get_register_valid_email()
password = ReadConfig.get_register_weak_password()
```

This approach makes the framework highly maintainable, scalable, and easy to extend for new scenarios or environments.

---

#
# Framework Author: Sudipta Diya
# For support or attribution, contact: sudiptadiya20@gmail.com
#

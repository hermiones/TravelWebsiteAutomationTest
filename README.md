# Travel Website Automation

Automated end-to-end testing for the BlazeDemo travel website using Python, Selenium, Pytest, and Allure reporting. Easily run tests locally or in CI/CD with GitHub Actions.

---

## 🚀 Features
- **Selenium WebDriver** automation for Chrome
- **Pytest** for test structure and fixtures
- **Allure** for beautiful test reports (screenshots on failure included)
- **Configurable** via `config.ini` (URL, credentials, etc.)
- **GitHub Actions** pipeline for CI/CD
- **Automatic screenshots** on test failure: If any test case fails, the framework will automatically capture a screenshot of the browser at the moment of failure and save it in the `Screenshots/` folder for easy debugging.

---

## 📁 Project Structure
```
├── Configurations/
│   └── config.ini           # All environment/test data
├── Pages/
│   ├── LoginPage.py         # Page Object Model for Login
│   ├── RegisterPage.py      # Page Object Model for Register
│   └── FlightBookingPage.py # Page Object Model for Booking
├── Testcases/
│   ├── test_Login.py        # Login test scenarios
│   ├── test_Register.py     # Registration test scenarios
│   ├── test_FlightBooking.py# Booking test scenarios
│   ├── conftest.py          # Pytest fixtures & hooks
│   └── Screenshots/         # Screenshots on failure
├── Utilities/
│   └── ReadProperties.py    # Config reader
├── requirement.txt          # Python dependencies
├── Jenkinsfile              # (Optional) Jenkins pipeline
├── .github/workflows/ci.yml # GitHub Actions pipeline
└── README.md                # This file
```

---

## ⚙️ Setup & Run Locally

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
   pip install -r requirement.txt
   pip install allure-pytest
   ```
4. **Edit `Configurations/config.ini`** with your test data.
5. **Run tests:**
   ```sh
   pytest --alluredir=allure-results
   ```
6. **View Allure report:**
   ```sh
   allure serve allure-results
   ```

---

## 🧪 Example Test Scenarios
- Valid login
- Invalid login (wrong password, blank fields, invalid email)
- Registration with valid/invalid data
- Flight booking flow
- UI element checks
- Screenshots on failure

---

## 🛠️ CI/CD with GitHub Actions
- Tests run automatically on every push or PR to `main`
- Allure results are uploaded as an artifact
- Chrome and ChromeDriver are installed in the pipeline

---

## 📸 Screenshots on Failure
If a test fails, a screenshot is saved in `Screenshots/FAIL_<testname>.png` for easy debugging.

---

## 📚 Tech Stack
- Python 3.12+
- Selenium
- Pytest
- Allure
- GitHub Actions

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

If you want to contribute to this framework, let's work together and make it even better! 🚀

If you have amazing ideas for automation, or want to collaborate on new features, let's connect!

---

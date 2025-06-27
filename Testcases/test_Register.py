from selenium.webdriver.common.by import By
from Utilities.ReadProperties import ReadConfig
from Pages.RegisterPage import RegisterPage
import pytest


# Validating the title of the webpage
def test_reg1(driver):
    driver.get(ReadConfig.get_base_url())
    assert driver.title == "BlazeDemo"


# Navigating to the homepage
def test_reg2(driver):
    driver.get(ReadConfig.get_base_url())
    driver.find_element(By.XPATH, "//a[contains(text(),'home')]").click()


# Register with valid credentials
def test_reg3(driver):
    driver.get(ReadConfig.get_base_url())
    reg_page = RegisterPage(driver)
    reg_page.go_to_register()
    reg_page.register(
        ReadConfig.get_username(),
        "ABC Corp",
        ReadConfig.get_username(),
        ReadConfig.get_password(),
        ReadConfig.get_password(),
    )


# Registration with blank fields
def test_reg4_blank_fields(driver):
    driver.get(ReadConfig.get_base_url())
    reg_page = RegisterPage(driver)
    reg_page.go_to_register()
    reg_page.register(
        ReadConfig.get_blank_email(),
        "",
        ReadConfig.get_blank_email(),
        ReadConfig.get_blank_password(),
        ReadConfig.get_blank_password(),
    )
    # Optionally, assert error message


# Registration with mismatched passwords
def test_reg5_mismatched_passwords(driver):
    driver.get(ReadConfig.get_base_url())
    reg_page = RegisterPage(driver)
    reg_page.go_to_register()
    reg_page.register(
        ReadConfig.get_incorrect_email(),
        "Test Company",
        ReadConfig.get_incorrect_email(),
        ReadConfig.get_password(),
        ReadConfig.get_incorrect_password(),
    )
    # Optionally, assert error message for password mismatch


# Registration with already registered email
def test_reg6_existing_email(driver):
    driver.get(ReadConfig.get_base_url())
    reg_page = RegisterPage(driver)
    reg_page.go_to_register()
    reg_page.register(
        ReadConfig.get_username(),
        "Test Company",
        ReadConfig.get_username(),
        ReadConfig.get_password(),
        ReadConfig.get_password(),
    )
    # Optionally, assert error message for duplicate email


# Registration with invalid email format
def test_reg7_invalid_email_format(driver):
    driver.get(ReadConfig.get_base_url())
    reg_page = RegisterPage(driver)
    reg_page.go_to_register()
    reg_page.register(
        "invalid-email-format",
        "Test Company",
        "invalid-email-format",
        ReadConfig.get_password(),
        ReadConfig.get_password(),
    )
    # Optionally, assert error message for invalid email


# Registration with long input values
def test_reg8_long_input(driver):
    driver.get(ReadConfig.get_base_url())
    reg_page = RegisterPage(driver)
    reg_page.go_to_register()
    long_str = "a" * 256
    reg_page.register(
        long_str + "@test.com",
        long_str,
        long_str + "@test.com",
        long_str,
        long_str,
    )
    # Optionally, assert error message for long input


@pytest.mark.parametrize(
    "name, company, email, password, confirm_password, description",
    [
        (ReadConfig.get_register_valid_username(), ReadConfig.get_register_valid_company(), ReadConfig.get_register_valid_email(), ReadConfig.get_register_valid_password(), ReadConfig.get_register_valid_confirm_password(), "Valid registration"),
        (ReadConfig.get_blank_email(), ReadConfig.get_register_valid_company(), ReadConfig.get_blank_email(), ReadConfig.get_blank_password(), ReadConfig.get_blank_password(), "Blank fields"),
        (ReadConfig.get_incorrect_email(), ReadConfig.get_register_valid_company(), ReadConfig.get_incorrect_email(), ReadConfig.get_password(), ReadConfig.get_incorrect_password(), "Mismatched passwords"),
        (ReadConfig.get_register_valid_username(), ReadConfig.get_register_valid_company(), ReadConfig.get_register_valid_username(), ReadConfig.get_register_valid_password(), ReadConfig.get_register_valid_password(), "Already registered email"),
        (ReadConfig.get_invalid_email(), ReadConfig.get_register_valid_company(), ReadConfig.get_invalid_email(), ReadConfig.get_register_valid_password(), ReadConfig.get_register_valid_password(), "Invalid email format"),
        (ReadConfig.get_register_long_username(), ReadConfig.get_register_long_company(), ReadConfig.get_register_long_email(), ReadConfig.get_register_long_password(), ReadConfig.get_register_long_password(), "Long input values"),
        (ReadConfig.get_register_special_username(), ReadConfig.get_register_special_company(), ReadConfig.get_register_special_email(), ReadConfig.get_register_special_password(), ReadConfig.get_register_special_password(), "Special characters in all fields"),
        (ReadConfig.get_register_valid_username(), ReadConfig.get_register_valid_company(), ReadConfig.get_register_valid_username(), ReadConfig.get_register_weak_password(), ReadConfig.get_register_weak_password(), "Weak password"),
        (ReadConfig.get_register_valid_username(), ReadConfig.get_register_valid_company(), ReadConfig.get_register_valid_username(), ReadConfig.get_register_whitespace_password(), ReadConfig.get_register_whitespace_password(), "Whitespace password"),
        (ReadConfig.get_register_sql_username(), ReadConfig.get_register_sql_company(), ReadConfig.get_register_sql_email(), ReadConfig.get_register_sql_password(), ReadConfig.get_register_sql_password(), "SQL injection attempt"),
        (ReadConfig.get_register_xss_username(), ReadConfig.get_register_xss_company(), ReadConfig.get_register_xss_email(), ReadConfig.get_register_xss_password(), ReadConfig.get_register_xss_password(), "XSS in password"),
        (ReadConfig.get_register_valid_username(), ReadConfig.get_register_valid_company(), ReadConfig.get_register_valid_username(), ReadConfig.get_register_numeric_password(), ReadConfig.get_register_numeric_password(), "Numeric password"),
        (ReadConfig.get_register_valid_username(), ReadConfig.get_register_valid_company(), ReadConfig.get_register_valid_username(), ReadConfig.get_register_common_password(), ReadConfig.get_register_common_password(), "Common password"),
        (ReadConfig.get_register_valid_username(), ReadConfig.get_register_valid_company(), ReadConfig.get_register_valid_username(), ReadConfig.get_register_uppercase_password(), ReadConfig.get_register_uppercase_password(), "All uppercase password"),
        (ReadConfig.get_register_valid_username(), ReadConfig.get_register_valid_company(), ReadConfig.get_register_valid_username(), ReadConfig.get_register_verylong_password(), ReadConfig.get_register_verylong_password(), "Very long password"),
        (ReadConfig.get_register_valid_username(), ReadConfig.get_register_valid_company(), ReadConfig.get_register_valid_username(), ReadConfig.get_register_symbols_password(), ReadConfig.get_register_symbols_password(), "Password with symbols and numbers"),
        (ReadConfig.get_register_valid_username(), ReadConfig.get_register_valid_company(), ReadConfig.get_register_valid_username(), ReadConfig.get_register_unicode_password(), ReadConfig.get_register_unicode_password(), "Unicode password"),
        (ReadConfig.get_register_valid_username(), ReadConfig.get_register_valid_company(), ReadConfig.get_register_valid_username(), ReadConfig.get_register_chinese_password(), ReadConfig.get_register_chinese_password(), "Chinese password"),
        (ReadConfig.get_register_valid_username(), ReadConfig.get_register_valid_company(), ReadConfig.get_register_valid_username(), ReadConfig.get_register_japanese_password(), ReadConfig.get_register_japanese_password(), "Japanese password"),
        (ReadConfig.get_register_valid_username(), ReadConfig.get_register_valid_company(), ReadConfig.get_register_valid_username(), ReadConfig.get_register_korean_password(), ReadConfig.get_register_korean_password(), "Korean password"),
        # Whitespace and control characters
        (
            ReadConfig.get_whitespace_email(),
            ReadConfig.get_whitespace_company(),
            ReadConfig.get_whitespace_email(),
            ReadConfig.get_password_with_space(),
            ReadConfig.get_password_with_space(),
            "Password with space"
        ),
        (
            ReadConfig.get_whitespace_email(),
            ReadConfig.get_whitespace_company(),
            ReadConfig.get_whitespace_email(),
            ReadConfig.get_password_with_newline(),
            ReadConfig.get_password_with_newline(),
            "Password with newline"
        ),
        (
            ReadConfig.get_whitespace_email(),
            ReadConfig.get_whitespace_company(),
            ReadConfig.get_whitespace_email(),
            ReadConfig.get_password_with_tab(),
            ReadConfig.get_password_with_tab(),
            "Password with tab"
        ),
        (
            ReadConfig.get_whitespace_email(),
            ReadConfig.get_whitespace_company(),
            ReadConfig.get_whitespace_email(),
            ReadConfig.get_password_with_carriage_return(),
            ReadConfig.get_password_with_carriage_return(),
            "Password with carriage return"
        ),
        (
            ReadConfig.get_whitespace_email(),
            ReadConfig.get_whitespace_company(),
            ReadConfig.get_whitespace_email(),
            ReadConfig.get_password_with_null_byte(),
            ReadConfig.get_password_with_null_byte(),
            "Password with null byte"
        ),
        (
            ReadConfig.get_whitespace_email(),
            ReadConfig.get_whitespace_company(),
            ReadConfig.get_whitespace_email(),
            ReadConfig.get_password_with_unicode_snowman(),
            ReadConfig.get_password_with_unicode_snowman(),
            "Password with unicode snowman"
        ),

        # Quotes and slashes
        (
            ReadConfig.get_quotes_email(),
            ReadConfig.get_quotes_company(),
            ReadConfig.get_quotes_email(),
            ReadConfig.get_password_with_single_quote(),
            ReadConfig.get_password_with_single_quote(),
            "Password with single quote"
        ),
        (
            ReadConfig.get_quotes_email(),
            ReadConfig.get_quotes_company(),
            ReadConfig.get_quotes_email(),
            ReadConfig.get_password_with_double_quote(),
            ReadConfig.get_password_with_double_quote(),
            "Password with double quote"
        ),
        (
            ReadConfig.get_quotes_email(),
            ReadConfig.get_quotes_company(),
            ReadConfig.get_quotes_email(),
            ReadConfig.get_password_with_slash(),
            ReadConfig.get_password_with_slash(),
            "Password with slash"
        ),
        (
            ReadConfig.get_quotes_email(),
            ReadConfig.get_quotes_company(),
            ReadConfig.get_quotes_email(),
            ReadConfig.get_password_with_backslash(),
            ReadConfig.get_password_with_backslash(),
            "Password with backslash"
        ),
        (
            ReadConfig.get_quotes_email(),
            ReadConfig.get_quotes_company(),
            ReadConfig.get_quotes_email(),
            ReadConfig.get_password_with_dot(),
            ReadConfig.get_password_with_dot(),
            "Password with dot"
        ),
        (
            ReadConfig.get_quotes_email(),
            ReadConfig.get_quotes_company(),
            ReadConfig.get_quotes_email(),
            ReadConfig.get_password_with_comma(),
            ReadConfig.get_password_with_comma(),
            "Password with comma"
        ),
        (
            ReadConfig.get_quotes_email(),
            ReadConfig.get_quotes_company(),
            ReadConfig.get_quotes_email(),
            ReadConfig.get_password_with_semicolon(),
            ReadConfig.get_password_with_semicolon(),
            "Password with semicolon"
        ),
        (
            ReadConfig.get_quotes_email(),
            ReadConfig.get_quotes_company(),
            ReadConfig.get_quotes_email(),
            ReadConfig.get_password_with_colon(),
            ReadConfig.get_password_with_colon(),
            "Password with colon"
        ),
        (
            ReadConfig.get_quotes_email(),
            ReadConfig.get_quotes_company(),
            ReadConfig.get_quotes_email(),
            ReadConfig.get_password_with_question_mark(),
            ReadConfig.get_password_with_question_mark(),
            "Password with question mark"
        ),

        # Brackets and braces
        (
            ReadConfig.get_brackets_email(),
            ReadConfig.get_brackets_company(),
            ReadConfig.get_brackets_email(),
            ReadConfig.get_password_with_brackets(),
            ReadConfig.get_password_with_brackets(),
            "Password with brackets"
        ),
        (
            ReadConfig.get_brackets_email(),
            ReadConfig.get_brackets_company(),
            ReadConfig.get_brackets_email(),
            ReadConfig.get_password_with_braces(),
            ReadConfig.get_password_with_braces(),
            "Password with braces"
        ),
        (
            ReadConfig.get_brackets_email(),
            ReadConfig.get_brackets_company(),
            ReadConfig.get_brackets_email(),
            ReadConfig.get_password_with_angle_brackets(),
            ReadConfig.get_password_with_angle_brackets(),
            "Password with angle brackets"
        ),
        (
            ReadConfig.get_brackets_email(),
            ReadConfig.get_brackets_company(),
            ReadConfig.get_brackets_email(),
            ReadConfig.get_password_with_pipe(),
            ReadConfig.get_password_with_pipe(),
            "Password with pipe"
        ),

        # Miscellaneous symbols
        (
            ReadConfig.get_misc_email(),
            ReadConfig.get_misc_company(),
            ReadConfig.get_misc_email(),
            ReadConfig.get_password_with_tilde(),
            ReadConfig.get_password_with_tilde(),
            "Password with tilde"
        ),
        (
            ReadConfig.get_misc_email(),
            ReadConfig.get_misc_company(),
            ReadConfig.get_misc_email(),
            ReadConfig.get_password_with_backtick(),
            ReadConfig.get_password_with_backtick(),
            "Password with backtick"
        ),
        (
            ReadConfig.get_misc_email(),
            ReadConfig.get_misc_company(),
            ReadConfig.get_misc_email(),
            ReadConfig.get_password_with_exclamation(),
            ReadConfig.get_password_with_exclamation(),
            "Password with exclamation"
        ),
        (
            ReadConfig.get_misc_email(),
            ReadConfig.get_misc_company(),
            ReadConfig.get_misc_email(),
            ReadConfig.get_password_with_at_symbol(),
            ReadConfig.get_password_with_at_symbol(),
            "Password with at symbol"
        ),
        (
            ReadConfig.get_misc_email(),
            ReadConfig.get_misc_company(),
            ReadConfig.get_misc_email(),
            ReadConfig.get_password_with_hash(),
            ReadConfig.get_password_with_hash(),
            "Password with hash"
        ),
        (
            ReadConfig.get_misc_email(),
            ReadConfig.get_misc_company(),
            ReadConfig.get_misc_email(),
            ReadConfig.get_password_with_dollar(),
            ReadConfig.get_password_with_dollar(),
            "Password with dollar"
        ),
        (
            ReadConfig.get_misc_email(),
            ReadConfig.get_misc_company(),
            ReadConfig.get_misc_email(),
            ReadConfig.get_password_with_percent(),
            ReadConfig.get_password_with_percent(),
            "Password with percent"
        ),
        (
            ReadConfig.get_misc_email(),
            ReadConfig.get_misc_company(),
            ReadConfig.get_misc_email(),
            ReadConfig.get_password_with_caret(),
            ReadConfig.get_password_with_caret(),
            "Password with caret"
        ),
        (
            ReadConfig.get_misc_email(),
            ReadConfig.get_misc_company(),
            ReadConfig.get_misc_email(),
            ReadConfig.get_password_with_ampersand(),
            ReadConfig.get_password_with_ampersand(),
            "Password with ampersand"
        ),
        (
            ReadConfig.get_misc_email(),
            ReadConfig.get_misc_company(),
            ReadConfig.get_misc_email(),
            ReadConfig.get_password_with_asterisk(),
            ReadConfig.get_password_with_asterisk(),
            "Password with asterisk"
        ),
        (
            ReadConfig.get_misc_email(),
            ReadConfig.get_misc_company(),
            ReadConfig.get_misc_email(),
            ReadConfig.get_password_with_parentheses(),
            ReadConfig.get_password_with_parentheses(),
            "Password with parentheses"
        ),
        (
            ReadConfig.get_misc_email(),
            ReadConfig.get_misc_company(),
            ReadConfig.get_misc_email(),
            ReadConfig.get_password_with_equals(),
            ReadConfig.get_password_with_equals(),
            "Password with equals"
        ),
        (
            ReadConfig.get_misc_email(),
            ReadConfig.get_misc_company(),
            ReadConfig.get_misc_email(),
            ReadConfig.get_password_with_plus(),
            ReadConfig.get_password_with_plus(),
            "Password with plus"
        ),
        (
            ReadConfig.get_misc_email(),
            ReadConfig.get_misc_company(),
            ReadConfig.get_misc_email(),
            ReadConfig.get_password_with_underscore(),
            ReadConfig.get_password_with_underscore(),
            "Password with underscore"
        ),
        (
            ReadConfig.get_misc_email(),
            ReadConfig.get_misc_company(),
            ReadConfig.get_misc_email(),
            ReadConfig.get_password_with_hyphen(),
            ReadConfig.get_password_with_hyphen(),
            "Password with hyphen"
        ),

        # Edge cases
        (
            ReadConfig.get_edge_email(),
            ReadConfig.get_edge_company(),
            ReadConfig.get_edge_email(),
            ReadConfig.get_password_with_letters(),
            ReadConfig.get_password_with_letters(),
            "Password with only letters"
        ),
        (
            ReadConfig.get_edge_email(),
            ReadConfig.get_edge_company(),
            ReadConfig.get_edge_email(),
            ReadConfig.get_password_with_numbers(),
            ReadConfig.get_password_with_numbers(),
            "Password with only numbers"
        ),
    ]
)
def test_register_parametrized(driver, name, company, email, password, confirm_password, description):
    driver.get(ReadConfig.get_base_url())
    reg_page = RegisterPage(driver)
    reg_page.go_to_register()
    reg_page.register(name, company, email, password, confirm_password)
    # Optionally, assert based on 'description' or expected outcome

import configparser
import os

class ReadConfig:
    # Loads the config file from the Configurations directory
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Configurations', 'config.ini')
    config = configparser.ConfigParser(interpolation=None)
    config.read(config_path, encoding="utf-8")

    @staticmethod
    def get_base_url():
        # Returns the base URL for the application
        return ReadConfig.config.get('DEFAULT', 'base_url')

    @staticmethod
    def get_browser():
        # Returns the browser type to use for tests
        return ReadConfig.config.get('DEFAULT', 'browser')

    @staticmethod
    def get_username():
        # Returns the login username
        return ReadConfig.config.get('LOGIN', 'username')

    @staticmethod
    def get_password():
        # Returns the login password
        return ReadConfig.config.get('LOGIN', 'password')

    @staticmethod
    def get_incorrect_email():
        # Returns an incorrect email for negative login tests
        return ReadConfig.config.get('LOGIN', 'incorrect_email')

    @staticmethod
    def get_incorrect_password():
        # Returns an incorrect password for negative login tests
        return ReadConfig.config.get('LOGIN', 'incorrect_password')

    @staticmethod
    def get_blank_email():
        # Returns a blank email value
        return ReadConfig.config.get('LOGIN', 'blank_email', fallback='')

    @staticmethod
    def get_blank_password():
        # Returns a blank password value
        return ReadConfig.config.get('LOGIN', 'blank_password', fallback='')

    @staticmethod
    def get_invalid_email():
        # Returns an invalid email format
        return ReadConfig.config.get('LOGIN', 'invalid_email', fallback='invalidemail')

    @staticmethod
    def get_test_email():
        # Returns a test email address
        return ReadConfig.config.get('LOGIN', 'test_email', fallback='test@example.com')

    @staticmethod
    def get_screenshot_dir():
        # Returns the directory path for saving screenshots
        return ReadConfig.config.get('PATHS', 'screenshot_dir')

    @staticmethod
    def get_register_valid_email():
        # Returns a valid email for registration
        return ReadConfig.config.get('REGISTER', 'valid_email')

    @staticmethod
    def get_register_valid_company():
        # Returns a valid company name for registration
        return ReadConfig.config.get('REGISTER', 'valid_company')

    @staticmethod
    def get_register_valid_username():
        # Returns a valid username for registration
        return ReadConfig.config.get('REGISTER', 'valid_username')

    @staticmethod
    def get_register_valid_password():
        # Returns a valid password for registration
        return ReadConfig.config.get('REGISTER', 'valid_password')

    @staticmethod
    def get_register_valid_confirm_password():
        # Returns a valid confirm password for registration
        return ReadConfig.config.get('REGISTER', 'valid_confirm_password')

    @staticmethod
    def get_register_long_email():
        # Returns a long email string for edge case testing
        return ReadConfig.config.get('REGISTER', 'long_email')

    @staticmethod
    def get_register_long_company():
        # Returns a long company name for edge case testing
        return ReadConfig.config.get('REGISTER', 'long_company')

    @staticmethod
    def get_register_long_username():
        # Returns a long username for edge case testing
        return ReadConfig.config.get('REGISTER', 'long_username')

    @staticmethod
    def get_register_long_password():
        # Returns a long password for edge case testing
        return ReadConfig.config.get('REGISTER', 'long_password')

    @staticmethod
    def get_register_special_email():
        # Returns an email with special characters
        return ReadConfig.config.get('REGISTER', 'special_email')

    @staticmethod
    def get_register_special_company():
        # Returns a company name with special characters
        return ReadConfig.config.get('REGISTER', 'special_company')

    @staticmethod
    def get_register_special_username():
        # Returns a username with special characters
        return ReadConfig.config.get('REGISTER', 'special_username')

    @staticmethod
    def get_register_special_password():
        # Returns a password with special characters
        return ReadConfig.config.get('REGISTER', 'special_password')

    @staticmethod
    def get_register_sql_email():
        # Returns an email with SQL injection pattern
        return ReadConfig.config.get('REGISTER', 'sql_email')

    @staticmethod
    def get_register_sql_company():
        # Returns a company name with SQL injection pattern
        return ReadConfig.config.get('REGISTER', 'sql_company')

    @staticmethod
    def get_register_sql_username():
        # Returns a username with SQL injection pattern
        return ReadConfig.config.get('REGISTER', 'sql_username')

    @staticmethod
    def get_register_sql_password():
        # Returns a password with SQL injection pattern
        return ReadConfig.config.get('REGISTER', 'sql_password')

    @staticmethod
    def get_register_xss_email():
        # Returns an email with XSS payload
        return ReadConfig.config.get('REGISTER', 'xss_email')

    @staticmethod
    def get_register_xss_company():
        # Returns a company name with XSS payload
        return ReadConfig.config.get('REGISTER', 'xss_company')

    @staticmethod
    def get_register_xss_username():
        # Returns a username with XSS payload
        return ReadConfig.config.get('REGISTER', 'xss_username')

    @staticmethod
    def get_register_xss_password():
        # Returns a password with XSS payload
        return ReadConfig.config.get('REGISTER', 'xss_password')

    @staticmethod
    def get_register_unicode_password():
        # Returns a password with unicode characters
        return ReadConfig.config.get('REGISTER', 'unicode_password')

    @staticmethod
    def get_register_chinese_password():
        # Returns a password with Chinese characters
        return ReadConfig.config.get('REGISTER', 'chinese_password')

    @staticmethod
    def get_register_japanese_password():
        # Returns a password with Japanese characters
        return ReadConfig.config.get('REGISTER', 'japanese_password')

    @staticmethod
    def get_register_korean_password():
        # Returns a password with Korean characters
        return ReadConfig.config.get('REGISTER', 'korean_password')

    @staticmethod
    def get_login_valid_username():
        # Returns a valid username for login tests
        return ReadConfig.config.get('LOGIN_TESTS', 'valid_username')

    @staticmethod
    def get_login_valid_password():
        # Returns a valid password for login tests
        return ReadConfig.config.get('LOGIN_TESTS', 'valid_password')

    @staticmethod
    def get_login_invalid_username():
        # Returns an invalid username for login tests
        return ReadConfig.config.get('LOGIN_TESTS', 'invalid_username')

    @staticmethod
    def get_login_invalid_password():
        # Returns an invalid password for login tests
        return ReadConfig.config.get('LOGIN_TESTS', 'invalid_password')

    @staticmethod
    def get_login_blank_username():
        # Returns a blank username for login tests
        return ReadConfig.config.get('LOGIN_TESTS', 'blank_username')

    @staticmethod
    def get_login_blank_password():
        # Returns a blank password for login tests
        return ReadConfig.config.get('LOGIN_TESTS', 'blank_password')

    @staticmethod
    def get_login_special_username():
        # Returns a username with special characters for login tests
        return ReadConfig.config.get('LOGIN_TESTS', 'special_username')

    @staticmethod
    def get_login_special_password():
        # Returns a password with special characters for login tests
        return ReadConfig.config.get('LOGIN_TESTS', 'special_password')

    @staticmethod
    def get_login_long_username():
        # Returns a long username for login tests
        return ReadConfig.config.get('LOGIN_TESTS', 'long_username')

    @staticmethod
    def get_login_long_password():
        # Returns a long password for login tests
        return ReadConfig.config.get('LOGIN_TESTS', 'long_password')

    @staticmethod
    def get_login_unicode_password():
        # Returns a password with unicode characters for login tests
        return ReadConfig.config.get('LOGIN_TESTS', 'unicode_password')

    @staticmethod
    def get_login_chinese_password():
        # Returns a password with Chinese characters for login tests
        return ReadConfig.config.get('LOGIN_TESTS', 'chinese_password')

    @staticmethod
    def get_login_japanese_password():
        # Returns a password with Japanese characters for login tests
        return ReadConfig.config.get('LOGIN_TESTS', 'japanese_password')

    @staticmethod
    def get_login_korean_password():
        # Returns a password with Korean characters for login tests
        return ReadConfig.config.get('LOGIN_TESTS', 'korean_password')

    @staticmethod
    def get_login_sql_username():
        # Returns a username with SQL injection pattern for login tests
        return ReadConfig.config.get('LOGIN_TESTS', 'sql_username')

    @staticmethod
    def get_login_sql_password():
        # Returns a password with SQL injection pattern for login tests
        return ReadConfig.config.get('LOGIN_TESTS', 'sql_password')

    @staticmethod
    def get_login_xss_username():
        # Returns a username with XSS payload for login tests
        return ReadConfig.config.get('LOGIN_TESTS', 'xss_username')

    @staticmethod
    def get_login_xss_password():
        # Returns a password with XSS payload for login tests
        return ReadConfig.config.get('LOGIN_TESTS', 'xss_password')

    @staticmethod
    def get_departure_cities():
        # Returns a list of departure cities for flight booking
        return [city.strip() for city in ReadConfig.config.get('FLIGHT_BOOKING', 'departure_cities').split(',')]

    @staticmethod
    def get_arrival_cities():
        # Returns a list of arrival cities for flight booking
        return [city.strip() for city in ReadConfig.config.get('FLIGHT_BOOKING', 'arrival_cities').split(',')]

    @staticmethod
    def get_passenger_names():
        # Returns a list of passenger names for flight booking
        return [name.strip() for name in ReadConfig.config.get('FLIGHT_BOOKING', 'passenger_names').split(',')]

    @staticmethod
    def get_passenger_addresses():
        # Returns a list of passenger addresses for flight booking
        return [addr.strip() for addr in ReadConfig.config.get('FLIGHT_BOOKING', 'passenger_addresses').split(',')]

    @staticmethod
    def get_passenger_cities():
        # Returns a list of passenger cities for flight booking
        return [city.strip() for city in ReadConfig.config.get('FLIGHT_BOOKING', 'passenger_cities').split(',')]

    @staticmethod
    def get_register_weak_password():
        # Returns a weak password for registration
        return ReadConfig.config.get('REGISTER', 'weak_password')

    @staticmethod
    def get_register_whitespace_password():
        # Returns a password with only whitespace
        return ReadConfig.config.get('REGISTER', 'whitespace_password')

    @staticmethod
    def get_register_numeric_password():
        # Returns a numeric password
        return ReadConfig.config.get('REGISTER', 'numeric_password')

    @staticmethod
    def get_register_common_password():
        # Returns a common password
        return ReadConfig.config.get('REGISTER', 'common_password')

    @staticmethod
    def get_register_uppercase_password():
        # Returns a password with only uppercase letters
        return ReadConfig.config.get('REGISTER', 'uppercase_password')

    @staticmethod
    def get_register_verylong_password():
        # Returns a very long password
        return ReadConfig.config.get('REGISTER', 'verylong_password')

    @staticmethod
    def get_register_symbols_password():
        # Returns a password with symbols
        return ReadConfig.config.get('REGISTER', 'symbols_password')

    @staticmethod
    def get_whitespace_email():
        # Returns an email with whitespace
        return ReadConfig.config.get('REGISTER', 'whitespace_email')

    @staticmethod
    def get_whitespace_company():
        # Returns a company name with whitespace
        return ReadConfig.config.get('REGISTER', 'whitespace_company')

    @staticmethod
    def get_password_with_space():
        # Returns a password containing a space
        return ReadConfig.config.get('REGISTER', 'password_with_space')

    @staticmethod
    def get_password_with_newline():
        # Returns a password containing a newline
        return ReadConfig.config.get('REGISTER', 'password_with_newline')

    @staticmethod
    def get_password_with_tab():
        # Returns a password containing a tab character
        return ReadConfig.config.get('REGISTER', 'password_with_tab')

    @staticmethod
    def get_password_with_carriage_return():
        # Returns a password containing a carriage return
        return ReadConfig.config.get('REGISTER', 'password_with_carriage_return')

    @staticmethod
    def get_password_with_null_byte():
        # Returns a password containing a null byte
        return ReadConfig.config.get('REGISTER', 'password_with_null_byte')

    @staticmethod
    def get_password_with_unicode_snowman():
        # Returns a password containing a unicode snowman character
        return ReadConfig.config.get('REGISTER', 'password_with_unicode_snowman')

    @staticmethod
    def get_quotes_email():
        # Returns an email with quotes
        return ReadConfig.config.get('REGISTER', 'quotes_email')

    @staticmethod
    def get_quotes_company():
        # Returns a company name with quotes
        return ReadConfig.config.get('REGISTER', 'quotes_company')

    @staticmethod
    def get_password_with_single_quote():
        # Returns a password containing a single quote
        return ReadConfig.config.get('REGISTER', 'password_with_single_quote')

    @staticmethod
    def get_password_with_double_quote():
        # Returns a password containing a double quote
        return ReadConfig.config.get('REGISTER', 'password_with_double_quote')

    @staticmethod
    def get_password_with_slash():
        # Returns a password containing a slash
        return ReadConfig.config.get('REGISTER', 'password_with_slash')

    @staticmethod
    def get_password_with_backslash():
        # Returns a password containing a backslash
        return ReadConfig.config.get('REGISTER', 'password_with_backslash')

    @staticmethod
    def get_password_with_dot():
        # Returns a password containing a dot
        return ReadConfig.config.get('REGISTER', 'password_with_dot')

    @staticmethod
    def get_password_with_comma():
        # Returns a password containing a comma
        return ReadConfig.config.get('REGISTER', 'password_with_comma')

    @staticmethod
    def get_password_with_semicolon():
        # Returns a password containing a semicolon
        return ReadConfig.config.get('REGISTER', 'password_with_semicolon')

    @staticmethod
    def get_password_with_colon():
        # Returns a password containing a colon
        return ReadConfig.config.get('REGISTER', 'password_with_colon')

    @staticmethod
    def get_password_with_question_mark():
        # Returns a password containing a question mark
        return ReadConfig.config.get('REGISTER', 'password_with_question_mark')

    @staticmethod
    def get_brackets_email():
        # Returns an email with brackets
        return ReadConfig.config.get('REGISTER', 'brackets_email')

    @staticmethod
    def get_brackets_company():
        # Returns a company name with brackets
        return ReadConfig.config.get('REGISTER', 'brackets_company')

    @staticmethod
    def get_password_with_brackets():
        # Returns a password containing brackets
        return ReadConfig.config.get('REGISTER', 'password_with_brackets')

    @staticmethod
    def get_password_with_braces():
        # Returns a password containing braces
        return ReadConfig.config.get('REGISTER', 'password_with_braces')

    @staticmethod
    def get_password_with_angle_brackets():
        # Returns a password containing angle brackets
        return ReadConfig.config.get('REGISTER', 'password_with_angle_brackets')

    @staticmethod
    def get_password_with_pipe():
        # Returns a password containing a pipe character
        return ReadConfig.config.get('REGISTER', 'password_with_pipe')

    @staticmethod
    def get_misc_email():
        # Returns a miscellaneous email for edge cases
        return ReadConfig.config.get('REGISTER', 'misc_email')

    @staticmethod
    def get_misc_company():
        # Returns a miscellaneous company name for edge cases
        return ReadConfig.config.get('REGISTER', 'misc_company')

    @staticmethod
    def get_password_with_tilde():
        # Returns a password containing a tilde
        return ReadConfig.config.get('REGISTER', 'password_with_tilde')

    @staticmethod
    def get_password_with_backtick():
        # Returns a password containing a backtick
        return ReadConfig.config.get('REGISTER', 'password_with_backtick')

    @staticmethod
    def get_password_with_exclamation():
        # Returns a password containing an exclamation mark
        return ReadConfig.config.get('REGISTER', 'password_with_exclamation')

    @staticmethod
    def get_password_with_at_symbol():
        # Returns a password containing an at symbol
        return ReadConfig.config.get('REGISTER', 'password_with_at_symbol')

    @staticmethod
    def get_password_with_hash():
        # Returns a password containing a hash symbol
        return ReadConfig.config.get('REGISTER', 'password_with_hash')

    @staticmethod
    def get_password_with_dollar():
        # Returns a password containing a dollar sign
        return ReadConfig.config.get('REGISTER', 'password_with_dollar')

    @staticmethod
    def get_password_with_percent():
        # Returns a password containing a percent sign
        return ReadConfig.config.get('REGISTER', 'password_with_percent')

    @staticmethod
    def get_password_with_caret():
        # Returns a password containing a caret
        return ReadConfig.config.get('REGISTER', 'password_with_caret')

    @staticmethod
    def get_password_with_ampersand():
        # Returns a password containing an ampersand
        return ReadConfig.config.get('REGISTER', 'password_with_ampersand')

    @staticmethod
    def get_password_with_asterisk():
        # Returns a password containing an asterisk
        return ReadConfig.config.get('REGISTER', 'password_with_asterisk')

    @staticmethod
    def get_password_with_parentheses():
        # Returns a password containing parentheses
        return ReadConfig.config.get('REGISTER', 'password_with_parentheses')

    @staticmethod
    def get_password_with_equals():
        # Returns a password containing an equals sign
        return ReadConfig.config.get('REGISTER', 'password_with_equals')

    @staticmethod
    def get_password_with_plus():
        # Returns a password containing a plus sign
        return ReadConfig.config.get('REGISTER', 'password_with_plus')

    @staticmethod
    def get_password_with_underscore():
        # Returns a password containing an underscore
        return ReadConfig.config.get('REGISTER', 'password_with_underscore')

    @staticmethod
    def get_password_with_hyphen():
        # Returns a password containing a hyphen
        return ReadConfig.config.get('REGISTER', 'password_with_hyphen')

    @staticmethod
    def get_edge_email():
        # Returns an edge case email
        return ReadConfig.config.get('REGISTER', 'edge_email')

    @staticmethod
    def get_edge_company():
        # Returns an edge case company name
        return ReadConfig.config.get('REGISTER', 'edge_company')

    @staticmethod
    def get_password_with_letters():
        # Returns a password with only letters
        return ReadConfig.config.get('REGISTER', 'password_with_letters')

    @staticmethod
    def get_password_with_numbers():
        # Returns a password with only numbers
        return ReadConfig.config.get('REGISTER', 'password_with_numbers')

    @staticmethod
    def get_weak_password():
        # Returns a weak password
        return ReadConfig.config.get('REGISTER', 'weak_password')

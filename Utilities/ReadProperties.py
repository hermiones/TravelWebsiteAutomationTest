import configparser
import os

class ReadConfig:
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Configurations', 'config.ini')
    config = configparser.ConfigParser()
    config.read(config_path)

    @staticmethod
    def get_base_url():
        return ReadConfig.config.get('DEFAULT', 'base_url')

    @staticmethod
    def get_browser():
        return ReadConfig.config.get('DEFAULT', 'browser')

    @staticmethod
    def get_username():
        return ReadConfig.config.get('LOGIN', 'username')

    @staticmethod
    def get_password():
        return ReadConfig.config.get('LOGIN', 'password')

    @staticmethod
    def get_incorrect_email():
        return ReadConfig.config.get('LOGIN', 'incorrect_email')

    @staticmethod
    def get_incorrect_password():
        return ReadConfig.config.get('LOGIN', 'incorrect_password')

    @staticmethod
    def get_blank_email():
        return ReadConfig.config.get('LOGIN', 'blank_email', fallback='')

    @staticmethod
    def get_blank_password():
        return ReadConfig.config.get('LOGIN', 'blank_password', fallback='')

    @staticmethod
    def get_invalid_email():
        return ReadConfig.config.get('LOGIN', 'invalid_email', fallback='invalidemail')

    @staticmethod
    def get_test_email():
        return ReadConfig.config.get('LOGIN', 'test_email', fallback='test@example.com')

    @staticmethod
    def get_screenshot_dir():
        return ReadConfig.config.get('PATHS', 'screenshot_dir')

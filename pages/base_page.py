from browser import Browser


class BasePage(Browser):
    def __init__(self):
        pass

    def method_verify_url(self, url):
        actual_url = self.driver.current_url
        expected_url = url
        assert actual_url == expected_url

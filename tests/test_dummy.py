import pytest


class TestDummy:

    @pytest.mark.usefixtures("init_driver")
    def test_dummy_func(self):
        self.driver.get("http://demostore.supersqa.com")



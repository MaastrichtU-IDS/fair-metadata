import pytest

from my_package.application import App


@pytest.fixture(autouse=True)
def app():
    return App()


class TestApplication(object):

    def test_return_value(self, app):
        assert app.get_hello_world("test") == "Hello World, test"

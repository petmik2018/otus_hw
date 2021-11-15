import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url", action="store", default="https://ya.ru"
    )

    parser.addoption(
        "--s_code", action="store", default="200"
    )

@pytest.fixture
def my_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    return request.config.getoption("--s_code")




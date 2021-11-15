def pytest_addoption(parser):
    parser.addoption(
        "--url", action="store", type=str, default="ya.ru"
    )

    parser.addoption(
        "--s_code", action="store", type=str, default="200"
    )

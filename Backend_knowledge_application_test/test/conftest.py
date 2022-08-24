import pytest
from src import create_app

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here

@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

"""
def pytest_addoption(parser):
    # ability to test API on different hosts
    parser.addoption("--host", action="store", default="http://localhost:5000")

@pytest.fixture(scope="session")
def host(request):
    return request.config.getoption("--host")

@pytest.fixture(scope="session")
def api_v1_host(host):
    return os.path.join(host, "api", "v1")


"""
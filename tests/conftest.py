import copy
import pytest
from fastapi.testclient import TestClient
from src import app as app_module


@pytest.fixture
def app():
    return app_module.app


@pytest.fixture
def client(app):
    with TestClient(app) as c:
        yield c


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset the in-memory activities dict before/after each test."""
    original = copy.deepcopy(app_module.activities)
    yield
    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(original))

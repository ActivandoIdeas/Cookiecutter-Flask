"""
Init test env
"""
from app import app
import pytest


@pytest.fixture
def app():
    """Create example instance"""
    return app


@pytest.fixture
def client(app):
    """Create client instance"""
    return app.test_client()

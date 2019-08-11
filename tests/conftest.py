import pytest

import ridaakh


@pytest.fixture
def app():
    return ridaakh.Ridaakh(templates_dir="tests/templates", debug=False)


@pytest.fixture
def client(app):
    return app.session()

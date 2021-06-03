import os
from unittest.mock import patch
import pytest
from flaskr import create_app
from ask_wiki.models import roberta


@pytest.fixture(autouse=True)
def app():
    def __init__(self):
        self.nlp = lambda input: [{'score':1,'answer':'Test'}]
        pass

    with patch.object(roberta.Answerer, '__init__', __init__):
        app = create_app()
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
    yield app

@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()

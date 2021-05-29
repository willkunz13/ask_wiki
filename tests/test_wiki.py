import pytest

def test_wiki_call(client):
    query = "What is Wosskow?"
    response = client.post('/search', data=query)
    assert response.status_code != 404
    assert response.data == b'Angel Investor'

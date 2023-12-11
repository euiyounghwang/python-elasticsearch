
import pytest

# https://pytest-with-eric.com/pytest-advanced/pytest-fastapi-testing/

@pytest.mark.skip(reason="no way of currently testing this")
def test_skip():
    assert 1 != 1
    
    
def test_api(mock_client):
    response = mock_client.get("/")
    assert response is not None
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
    
    
def test_CRUD_api(mock_client):
    sample_payload = {
        "include_basic_aggs": True,
        "pit_id": "",
        "query_string": "performance",
        "size": 20,
        "sort_order": "DESC",
        "start_date": "2021 01-01 00:00:00"
    }
    
    # Create Item
    response = mock_client.post("/es/search", json=sample_payload)
    assert response.status_code == 200
    # assert response.json() == {
    #     "message ": "OK - Successful Query executed",
    #     "uuid": response.json()['uuid']
    # }
    
    
    
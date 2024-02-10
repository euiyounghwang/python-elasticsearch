
import pytest


def test_rest_api(mock_client):
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
    assert response.json()['total'] == {
        "value": 1,
        "relation": "eq"
    }
    
    
    
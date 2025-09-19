import json
import pytest
from fastapi.testclient import TestClient
from genoai_pathogenicity_engine.app import app

# Create a client to interact with your FastAPI app
client = TestClient(app)

@pytest.fixture
def comprehensive_test_payload():
    """A pytest fixture to load the comprehensive 6-variant test data from a JSON file."""
    # Note: Make sure the test_data.json file is in the same 'tests' directory
    with open("tests/test_data.json", "r") as f:
        return json.load(f)

def test_read_mcp_manifest():
    """Tests if the /mcp endpoint is available and returns a valid manifest."""
    response = client.get("/mcp")
    assert response.status_code == 200
    assert "mcp_version" in response.json()

def test_analyze_endpoint_with_comprehensive_payload(comprehensive_test_payload):
    """
    Tests a valid request to the /analyze/ endpoint using the full,
    realistic 6-variant payload.
    """
    # Send the loaded JSON data to the /analyze/ endpoint
    response = client.post("/analyze/", json=comprehensive_test_payload)

    # 1. Check for a successful response
    assert response.status_code == 200

    # 2. Check the structure of the response
    response_data = response.json()
    assert isinstance(response_data, list)
    assert len(response_data) == 6  # Ensure all 6 variants were processed and returned

    # 3. Check for the presence of your engine's output in the results
    assert "pathogenicity_score" in response_data[0]
    assert "pathogenicity_category" in response_data[0]

def test_analyze_endpoint_requires_data():
    """Tests that sending an empty JSON body results in a validation error."""
    response = client.post("/analyze/", json=[])
    # FastAPI's default for a required body that is empty is 422 Unprocessable Entity
    assert response.status_code == 422
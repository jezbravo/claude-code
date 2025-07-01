import pytest


@pytest.mark.asyncio
async def test_root_endpoint(client):
    """Test the root endpoint."""
    response = await client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Hello World"
    assert data["app"] == "Claude Code API"


@pytest.mark.asyncio
async def test_health_check(client):
    """Test the health check endpoint."""
    response = await client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"


@pytest.mark.asyncio
async def test_create_app(client):
    """Test creating a new app."""
    app_data = {
        "name": "Test App",
        "description": "A test application",
        "db_name": "test_db",
        "environment": "test",
        "wallet_id": 123,
        "status": "active"
    }
    
    response = await client.post("/apps/", json=app_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == app_data["name"]
    assert data["description"] == app_data["description"]
    assert data["environment"] == app_data["environment"]
    assert "id" in data
    assert "created_at" in data


@pytest.mark.asyncio
async def test_read_apps(client):
    """Test reading all apps."""
    # First create an app
    app_data = {
        "name": "Test App 2",
        "description": "Another test application",
        "db_name": "test_db_2",
        "environment": "test",
        "wallet_id": 456,
        "status": "active"
    }
    await client.post("/apps/", json=app_data)
    
    # Then read all apps
    response = await client.get("/apps/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1


@pytest.mark.asyncio
async def test_read_app_not_found(client):
    """Test reading a non-existent app."""
    response = await client.get("/apps/999")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "App not found"
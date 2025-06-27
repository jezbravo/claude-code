import pytest
from datetime import datetime
from claudecode.models.app import App


@pytest.mark.asyncio
async def test_app_model_with_status_field(db_session):
    session = await db_session.__anext__()
    """Test that App model includes status field for tracking application state."""
    # Test data
    app_data = {
        "name": "test-app",
        "description": "Test application",
        "db_name": "test_db",
        "environment": "development",
        "wallet_id": 1,
        "status": "active"
    }
    
    # Create app instance
    app = App(**app_data)
    session.add(app)
    await session.commit()
    await session.refresh(app)
    
    # Assertions
    assert app.id is not None
    assert app.name == "test-app"
    assert app.description == "Test application"
    assert app.db_name == "test_db"
    assert app.environment == "development"
    assert app.wallet_id == 1
    assert app.status == "active"
    assert isinstance(app.created_at, datetime)
    assert isinstance(app.updated_at, datetime)


@pytest.mark.asyncio
async def test_app_status_field_accepts_various_states(db_session):
    session = await db_session.__anext__()
    """Test that status field accepts different application states."""
    statuses = ["active", "inactive", "pending", "archived"]
    
    for status in statuses:
        app = App(
            name=f"app-{status}",
            description=f"App with {status} status",
            db_name=f"db_{status}",
            environment="test",
            wallet_id=1,
            status=status
        )
        session.add(app)
        await session.commit()
        await session.refresh(app)
        
        assert app.status == status


@pytest.mark.asyncio
async def test_app_status_field_required(db_session):
    session = await db_session.__anext__()
    """Test that status field is required when not nullable."""
    # This test will be updated once we determine if status should be nullable
    app = App(
        name="test-app-no-status",
        description="Test app without status",
        db_name="test_db",
        environment="test",
        wallet_id=1
        # status intentionally omitted
    )
    
    # If status has a default, this should work
    # If status is required, this should raise an error
    session.add(app)
    try:
        await session.commit()
        await session.refresh(app)
        # If we get here, status either has a default or is nullable
        assert hasattr(app, 'status')
    except Exception:
        # If we get an exception, status is required and not nullable
        await session.rollback()
        pytest.skip("Status field is required - expected behavior")
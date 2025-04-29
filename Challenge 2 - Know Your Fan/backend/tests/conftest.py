import pytest
from app import create_app, db
from app.models.user import User
from app.models.fan import Fan
from app.models.campaign import Campaign
from app.models.analytics import Analytics

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def test_user(app):
    user = User(
        full_name='Test User',
        email='test@example.com',
        password='password123'
    )
    db.session.add(user)
    db.session.commit()
    return user

@pytest.fixture
def test_fan(app):
    fan = Fan(
        name='Test Fan',
        email='fan@example.com',
        location='Test Location',
        engagement_score=0.5
    )
    db.session.add(fan)
    db.session.commit()
    return fan

@pytest.fixture
def test_campaign(app):
    campaign = Campaign(
        name='Test Campaign',
        description='Test Description',
        target_audience={'location': 'Test Location', 'engagement_score': 0.3}
    )
    db.session.add(campaign)
    db.session.commit()
    return campaign 
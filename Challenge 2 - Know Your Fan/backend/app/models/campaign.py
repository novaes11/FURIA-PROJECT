from app import db
from datetime import datetime

class Campaign(db.Model):
    __tablename__ = 'campaigns'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    target_audience = db.Column(db.JSON)  # Criteria for targeting fans
    status = db.Column(db.String(20), default='draft')  # draft, active, completed, cancelled
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __init__(self, name, description=None, target_audience=None, start_date=None, end_date=None):
        self.name = name
        self.description = description
        self.target_audience = target_audience or {}
        self.start_date = start_date
        self.end_date = end_date
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'target_audience': self.target_audience,
            'status': self.status,
            'start_date': self.start_date.isoformat() if self.start_date else None,
            'end_date': self.end_date.isoformat() if self.end_date else None,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
    
    def is_active(self):
        now = datetime.utcnow()
        return (
            self.status == 'active' and
            (not self.start_date or self.start_date <= now) and
            (not self.end_date or self.end_date >= now)
        ) 
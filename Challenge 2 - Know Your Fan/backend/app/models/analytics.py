from app import db
from datetime import datetime

class Analytics(db.Model):
    __tablename__ = 'analytics'
    
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)  # engagement, demographics, interactions, growth
    data = db.Column(db.JSON, nullable=False)
    period = db.Column(db.String(20), nullable=False)  # daily, weekly, monthly
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __init__(self, type, data, period):
        self.type = type
        self.data = data
        self.period = period
    
    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'data': self.data,
            'period': self.period,
            'created_at': self.created_at.isoformat()
        } 
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.models.analytics import Analytics
from app.models.fan import Fan
from app import db
from datetime import datetime, timedelta
import json

analytics_bp = Blueprint('analytics', __name__)

def calculate_engagement_metrics():
    # Calculate engagement metrics based on fan interactions
    fans = Fan.query.all()
    total_fans = len(fans)
    active_fans = sum(1 for fan in fans if fan.engagement_score > 0)
    avg_engagement = sum(fan.engagement_score for fan in fans) / total_fans if total_fans > 0 else 0
    
    return {
        'total_fans': total_fans,
        'active_fans': active_fans,
        'engagement_rate': (active_fans / total_fans * 100) if total_fans > 0 else 0,
        'average_engagement': avg_engagement
    }

def calculate_demographics():
    # Calculate demographic metrics based on fan locations
    fans = Fan.query.all()
    locations = {}
    
    for fan in fans:
        if fan.location:
            locations[fan.location] = locations.get(fan.location, 0) + 1
    
    return {
        'total_fans': len(fans),
        'locations': locations
    }

def calculate_interactions():
    # Calculate interaction metrics based on fan engagement
    fans = Fan.query.all()
    interactions = {
        'high_engagement': sum(1 for fan in fans if fan.engagement_score >= 0.7),
        'medium_engagement': sum(1 for fan in fans if 0.3 <= fan.engagement_score < 0.7),
        'low_engagement': sum(1 for fan in fans if fan.engagement_score < 0.3)
    }
    
    return interactions

def calculate_growth():
    # Calculate growth metrics based on fan creation dates
    fans = Fan.query.all()
    now = datetime.utcnow()
    last_month = now - timedelta(days=30)
    
    new_fans = sum(1 for fan in fans if fan.created_at >= last_month)
    total_fans = len(fans)
    
    return {
        'total_fans': total_fans,
        'new_fans_last_month': new_fans,
        'growth_rate': (new_fans / total_fans * 100) if total_fans > 0 else 0
    }

@analytics_bp.route('/engagement', methods=['GET'])
@jwt_required()
def get_engagement_analytics():
    data = calculate_engagement_metrics()
    analytics = Analytics(
        type='engagement',
        data=data,
        period='daily'
    )
    
    try:
        db.session.add(analytics)
        db.session.commit()
        return jsonify(analytics.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Error saving analytics'}), 500

@analytics_bp.route('/demographics', methods=['GET'])
@jwt_required()
def get_demographics_analytics():
    data = calculate_demographics()
    analytics = Analytics(
        type='demographics',
        data=data,
        period='monthly'
    )
    
    try:
        db.session.add(analytics)
        db.session.commit()
        return jsonify(analytics.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Error saving analytics'}), 500

@analytics_bp.route('/interactions', methods=['GET'])
@jwt_required()
def get_interactions_analytics():
    data = calculate_interactions()
    analytics = Analytics(
        type='interactions',
        data=data,
        period='weekly'
    )
    
    try:
        db.session.add(analytics)
        db.session.commit()
        return jsonify(analytics.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Error saving analytics'}), 500

@analytics_bp.route('/growth', methods=['GET'])
@jwt_required()
def get_growth_analytics():
    data = calculate_growth()
    analytics = Analytics(
        type='growth',
        data=data,
        period='monthly'
    )
    
    try:
        db.session.add(analytics)
        db.session.commit()
        return jsonify(analytics.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Error saving analytics'}), 500 
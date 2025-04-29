from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.models.campaign import Campaign
from app.models.fan import Fan
from app import db
from datetime import datetime

campaigns_bp = Blueprint('campaigns', __name__)

@campaigns_bp.route('/', methods=['GET'])
@jwt_required()
def get_campaigns():
    campaigns = Campaign.query.all()
    return jsonify([campaign.to_dict() for campaign in campaigns]), 200

@campaigns_bp.route('/<int:campaign_id>', methods=['GET'])
@jwt_required()
def get_campaign(campaign_id):
    campaign = Campaign.query.get_or_404(campaign_id)
    return jsonify(campaign.to_dict()), 200

@campaigns_bp.route('/', methods=['POST'])
@jwt_required()
def create_campaign():
    data = request.get_json()
    
    # Validate required fields
    if not all(k in data for k in ('name',)):
        return jsonify({'error': 'Missing required fields'}), 400
    
    # Parse dates if provided
    start_date = None
    end_date = None
    if 'start_date' in data:
        start_date = datetime.fromisoformat(data['start_date'])
    if 'end_date' in data:
        end_date = datetime.fromisoformat(data['end_date'])
    
    # Create new campaign
    campaign = Campaign(
        name=data['name'],
        description=data.get('description'),
        target_audience=data.get('target_audience'),
        start_date=start_date,
        end_date=end_date
    )
    
    try:
        db.session.add(campaign)
        db.session.commit()
        return jsonify(campaign.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Error creating campaign'}), 500

@campaigns_bp.route('/<int:campaign_id>', methods=['PUT'])
@jwt_required()
def update_campaign(campaign_id):
    campaign = Campaign.query.get_or_404(campaign_id)
    data = request.get_json()
    
    # Update campaign fields
    if 'name' in data:
        campaign.name = data['name']
    if 'description' in data:
        campaign.description = data['description']
    if 'target_audience' in data:
        campaign.target_audience = data['target_audience']
    if 'status' in data:
        campaign.status = data['status']
    if 'start_date' in data:
        campaign.start_date = datetime.fromisoformat(data['start_date'])
    if 'end_date' in data:
        campaign.end_date = datetime.fromisoformat(data['end_date'])
    
    try:
        db.session.commit()
        return jsonify(campaign.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Error updating campaign'}), 500

@campaigns_bp.route('/<int:campaign_id>', methods=['DELETE'])
@jwt_required()
def delete_campaign(campaign_id):
    campaign = Campaign.query.get_or_404(campaign_id)
    
    try:
        db.session.delete(campaign)
        db.session.commit()
        return jsonify({'message': 'Campaign deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Error deleting campaign'}), 500

@campaigns_bp.route('/<int:campaign_id>/target-audience', methods=['GET'])
@jwt_required()
def get_target_audience(campaign_id):
    campaign = Campaign.query.get_or_404(campaign_id)
    fans = Fan.query.all()
    
    # Filter fans based on campaign target audience criteria
    target_fans = []
    for fan in fans:
        matches = True
        for key, value in campaign.target_audience.items():
            if key == 'location' and fan.location != value:
                matches = False
                break
            elif key == 'engagement_score' and fan.engagement_score < value:
                matches = False
                break
        
        if matches:
            target_fans.append(fan.to_dict())
    
    return jsonify({
        'campaign': campaign.to_dict(),
        'target_audience': target_fans
    }), 200 
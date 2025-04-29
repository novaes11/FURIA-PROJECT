from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.fan import Fan
from app import db

fans_bp = Blueprint('fans', __name__)

@fans_bp.route('/', methods=['GET'])
@jwt_required()
def get_fans():
    fans = Fan.query.all()
    return jsonify([fan.to_dict() for fan in fans]), 200

@fans_bp.route('/<int:fan_id>', methods=['GET'])
@jwt_required()
def get_fan(fan_id):
    fan = Fan.query.get_or_404(fan_id)
    return jsonify(fan.to_dict()), 200

@fans_bp.route('/', methods=['POST'])
@jwt_required()
def create_fan():
    data = request.get_json()
    
    # Validate required fields
    if not all(k in data for k in ('name', 'email')):
        return jsonify({'error': 'Missing required fields'}), 400
    
    # Check if fan already exists
    if Fan.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email already registered'}), 400
    
    # Create new fan
    fan = Fan(
        name=data['name'],
        email=data['email'],
        location=data.get('location')
    )
    
    try:
        db.session.add(fan)
        db.session.commit()
        return jsonify(fan.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Error creating fan'}), 500

@fans_bp.route('/<int:fan_id>', methods=['PUT'])
@jwt_required()
def update_fan(fan_id):
    fan = Fan.query.get_or_404(fan_id)
    data = request.get_json()
    
    # Update fan fields
    if 'name' in data:
        fan.name = data['name']
    if 'email' in data:
        fan.email = data['email']
    if 'location' in data:
        fan.location = data['location']
    if 'engagement_score' in data:
        fan.engagement_score = data['engagement_score']
    
    try:
        db.session.commit()
        return jsonify(fan.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Error updating fan'}), 500

@fans_bp.route('/<int:fan_id>', methods=['DELETE'])
@jwt_required()
def delete_fan(fan_id):
    fan = Fan.query.get_or_404(fan_id)
    
    try:
        db.session.delete(fan)
        db.session.commit()
        return jsonify({'message': 'Fan deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Error deleting fan'}), 500 
from sqlalchemy import Column, Integer, String, Float, DateTime, JSON, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class FanProfile(Base):
    """Modelo para o perfil de fãs"""
    __tablename__ = "fan_profiles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    location = Column(String)
    gender = Column(String)
    interests = Column(JSON)
    social_media = Column(JSON)
    engagement_score = Column(Float)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    # Relacionamentos
    social_media_data = relationship("SocialMediaData", back_populates="fan_profile")
    interactions = relationship("FanInteraction", back_populates="fan_profile")

class SocialMediaData(Base):
    """Modelo para dados de redes sociais"""
    __tablename__ = "social_media_data"

    id = Column(Integer, primary_key=True, index=True)
    fan_profile_id = Column(Integer, ForeignKey("fan_profiles.id"))
    platform = Column(String)
    username = Column(String)
    followers = Column(Integer)
    posts = Column(Integer)
    engagement_rate = Column(Float)
    last_updated = Column(DateTime, default=datetime.now)

    # Relacionamentos
    fan_profile = relationship("FanProfile", back_populates="social_media_data")

class FanInteraction(Base):
    """Modelo para interações dos fãs"""
    __tablename__ = "fan_interactions"

    id = Column(Integer, primary_key=True, index=True)
    fan_profile_id = Column(Integer, ForeignKey("fan_profiles.id"))
    interaction_type = Column(String)  # post, like, comment, etc
    platform = Column(String)
    content = Column(String)
    timestamp = Column(DateTime, default=datetime.now)
    sentiment_score = Column(Float)  # Análise de sentimento

    # Relacionamentos
    fan_profile = relationship("FanProfile", back_populates="interactions")

class Campaign(Base):
    """Modelo para campanhas"""
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    target_audience = Column(JSON)  # Critérios de público-alvo
    metrics = Column(JSON)  # Métricas de sucesso
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now) 
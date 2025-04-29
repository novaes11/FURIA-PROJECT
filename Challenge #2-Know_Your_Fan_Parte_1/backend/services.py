from sqlalchemy.orm import Session
from . import models
from datetime import datetime
import numpy as np
from typing import List, Dict, Any
import json

class FanService:
    """Serviço para gerenciamento de perfis de fãs"""

    @staticmethod
    def calculate_engagement_score(social_media_data: Dict[str, Any]) -> float:
        """Calcula o score de engajamento baseado nos dados de redes sociais"""
        weights = {
            'followers': 0.3,
            'posts': 0.2,
            'engagement_rate': 0.5
        }
        
        score = 0
        for platform, data in social_media_data.items():
            platform_score = (
                data.get('followers', 0) * weights['followers'] +
                data.get('posts', 0) * weights['posts'] +
                data.get('engagement_rate', 0) * weights['engagement_rate']
            )
            score += platform_score
        
        return min(score / len(social_media_data), 1.0)

    @staticmethod
    def create_fan_profile(db: Session, profile_data: Dict[str, Any]) -> models.FanProfile:
        """Cria um novo perfil de fã"""
        # Calcula o score de engajamento
        engagement_score = FanService.calculate_engagement_score(profile_data.get('social_media', {}))
        
        # Cria o perfil
        fan_profile = models.FanProfile(
            name=profile_data['name'],
            age=profile_data['age'],
            location=profile_data['location'],
            gender=profile_data['gender'],
            interests=profile_data['interests'],
            social_media=profile_data['social_media'],
            engagement_score=engagement_score
        )
        
        db.add(fan_profile)
        db.commit()
        db.refresh(fan_profile)
        return fan_profile

    @staticmethod
    def get_fan_profile(db: Session, fan_id: int) -> models.FanProfile:
        """Obtém um perfil de fã pelo ID"""
        return db.query(models.FanProfile).filter(models.FanProfile.id == fan_id).first()

    @staticmethod
    def update_fan_profile(db: Session, fan_id: int, profile_data: Dict[str, Any]) -> models.FanProfile:
        """Atualiza um perfil de fã"""
        fan_profile = FanService.get_fan_profile(db, fan_id)
        if not fan_profile:
            return None
        
        # Atualiza os campos
        for key, value in profile_data.items():
            if hasattr(fan_profile, key):
                setattr(fan_profile, key, value)
        
        # Recalcula o score de engajamento
        fan_profile.engagement_score = FanService.calculate_engagement_score(
            fan_profile.social_media
        )
        
        db.commit()
        db.refresh(fan_profile)
        return fan_profile

class AnalyticsService:
    """Serviço para análise de dados dos fãs"""

    @staticmethod
    def get_engagement_analytics(db: Session) -> Dict[str, Any]:
        """Obtém análises de engajamento"""
        # Obtém todos os perfis
        profiles = db.query(models.FanProfile).all()
        
        # Calcula métricas
        total_fans = len(profiles)
        average_engagement = np.mean([p.engagement_score for p in profiles])
        
        # Análise por plataforma
        platform_engagement = {}
        for profile in profiles:
            for platform, data in profile.social_media.items():
                if platform not in platform_engagement:
                    platform_engagement[platform] = []
                platform_engagement[platform].append(data.get('engagement_rate', 0))
        
        # Calcula médias por plataforma
        platform_averages = {
            platform: np.mean(engagement_rates)
            for platform, engagement_rates in platform_engagement.items()
        }
        
        # Ordena plataformas por engajamento
        top_platforms = sorted(
            platform_averages.items(),
            key=lambda x: x[1],
            reverse=True
        )[:3]
        
        return {
            "total_fans": total_fans,
            "average_engagement": float(average_engagement),
            "top_platforms": [platform for platform, _ in top_platforms],
            "platform_engagement": {
                platform: float(avg)
                for platform, avg in platform_averages.items()
            }
        }

    @staticmethod
    def get_fan_segments(db: Session) -> Dict[str, Any]:
        """Analisa e retorna segmentos de fãs"""
        profiles = db.query(models.FanProfile).all()
        
        # Define critérios de segmentação
        segments = {
            "super_fans": [],
            "engaged_fans": [],
            "casual_fans": []
        }
        
        for profile in profiles:
            if profile.engagement_score >= 0.8:
                segments["super_fans"].append(profile.id)
            elif profile.engagement_score >= 0.5:
                segments["engaged_fans"].append(profile.id)
            else:
                segments["casual_fans"].append(profile.id)
        
        return {
            "segments": {
                name: len(fans)
                for name, fans in segments.items()
            },
            "total_fans": len(profiles)
        } 
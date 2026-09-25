
from typing import Optional, List
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.database.models import HeadOfSpecifications, CardOfArticle, GroupOfArticle
from app.database import SessionLocal


class AccessService:
    def __init__(self, db: Session):
        self.db = db

    def SpecificationFind(self, article: int) -> Optional[HeadOfSpecifications]:
        return self.db.query(HeadOfSpecifications).filter(
            HeadOfSpecifications.KA2450_REZ_NR == article 
        ).first()

    def CheckArticleCard(self, article: int) -> Optional[CardOfArticle]:
        return self.db.query(CardOfArticle).filter(
            CardOfArticle.SY0012_NR == article
        ).first()


    def CheckGroupOfSort(self, article: int) -> Optional[GroupOfArticle]:
        return self.db.query(GroupOfArticle).filter(
            GroupOfArticle.SY8081_ART_NR == article
        ).first()


    def getValidationStatus(self, article: int) -> dict:
        specification = self.SpecificationFind(article)
        CheckArticleCard = self.CheckArticleCard(article)
        GroupSort = self.CheckGroupOfSort(article)
        return {
            "article": article,
            "is valud": bool(specification and CheckArticleCard and GroupSort),
            "details" : {
                "has_specification": specification is not None,
                "destination": CheckArticleCard.SY0012_LAGER_NR is not None,
                "shelf_life": CheckArticleCard.SY0012_HBK_ZEIT is not None,
                "has_group_of_sort": GroupSort is not None
            }
        }
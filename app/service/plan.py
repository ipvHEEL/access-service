
from typing import Optional, List
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.database.models import HeadOfSpecifications, CardOfArticle, GroupOfArticle, BlockedArt
from app.database import SessionLocal
import datetime


class PlanService:
    def __init__(self, db: Session):
        self.db = db

    def getArtData(self, article: int) -> Optional[CardOfArticle]:
        art = self.db.query(CardOfArticle).filter(
            CardOfArticle.SY0012_NR == article
        ).first() 

        is_blocked = self.db.query(BlockedArt).filter(
            BlockedArt.SY8212_ART_NR == article
        ).first() 
        now_str = datetime.datetime.now().strftime("%Y%m%d")
        von = is_blocked.SY8212_DATUM_VON  
        bis = is_blocked.SY8212_DATUM_BIS 
        is_block = int(von) <= int(now_str) <= int(bis)
        # print(is_block)
        # print(is_blocked.SY8212_DATUM_VON, is_blocked.SY8212_DATUM_BIS)
        # print(datetime.datetime.now())
        # now = datetime.datetime.now()
        # print(now.strftime("%y%m%d"))
        return {
            "article": art.SY0012_NR,
            'article_sg': art.SY0012_HBK_ZEIT,
            'article_group': art.SY0012_ART_GRUPPE,
            'article_block': is_block
        }



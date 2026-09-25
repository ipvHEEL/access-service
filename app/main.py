from fastapi import FastAPI, Depends 
from sqlalchemy.orm import Session  
from app.database import get_db
from app.service.access import AccessService
from app.service.plan import PlanService

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Service is running"}


@app.get("/checkArticleValidation")
def check_art(article: int, db: Session = Depends(get_db)):
    access_service = AccessService(db)
    return access_service.getValidationStatus(article)
    
@app.get("/chekPlanValidation")
def check(article: int, db: Session = Depends(get_db)):
    plan_service = PlanService(db)
    return plan_service.getArtData(article)
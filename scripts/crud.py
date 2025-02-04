from sqlalchemy.orm import Session
from scripts.models import TelegramData, ObjectDetectionResult
from scripts.schemas import TelegramDataCreate, DetectionResultCreate

# Telegram Data CRUD
def get_telegram_data(db: Session, skip: int = 0, limit: int = 100):
    return db.query(TelegramData).offset(skip).limit(limit).all()

def get_telegram_message(db: Session, message_id: int):
    return db.query(TelegramData).filter(TelegramData.id == message_id).first()

# Detection Results CRUD
def get_detection_results(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ObjectDetectionResult).offset(skip).limit(limit).all()

def get_detection_result(db: Session, result_id: int):
    return db.query(ObjectDetectionResult).filter(ObjectDetectionResult.id == result_id).first()
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from fastapi import FastAPI, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from scripts.database import get_db
from scripts.models import TelegramData, ObjectDetectionResult
from scripts.schemas import TelegramData, DetectionResult
from scripts.crud import get_telegram_data, get_telegram_message, get_detection_results, get_detection_result

app = FastAPI()

# Telegram Data Endpoints
@app.get("/telegram-messages/", response_model=List[TelegramData])
def read_telegram_messages(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    messages = get_telegram_data(db, skip=skip, limit=limit)
    return messages

@app.get("/telegram-messages/{message_id}", response_model=TelegramData)
def read_telegram_message(message_id: int, db: Session = Depends(get_db)):
    message = get_telegram_message(db, message_id=message_id)
    if not message:
        raise HTTPException(status_code=404, detail="Message not found")
    return message

# Detection Results Endpoints
@app.get("/detections/", response_model=List[DetectionResult])
def read_detections(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    detections = get_detection_results(db, skip=skip, limit=limit)
    return detections

@app.get("/detections/{result_id}", response_model=DetectionResult)
def read_detection(result_id: int, db: Session = Depends(get_db)):
    detection = get_detection_result(db, result_id=result_id)
    if not detection:
        raise HTTPException(status_code=404, detail="Detection result not found")
    return detection
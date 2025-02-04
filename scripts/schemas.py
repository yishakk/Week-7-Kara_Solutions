from pydantic import BaseModel
from datetime import datetime

# Telegram Data Schemas
class TelegramDataBase(BaseModel):
    id: int
    message_id: int
    channel_title: str
    channel_username: str
    message : str
    message_date: datetime
    media_path: str

class TelegramDataCreate(TelegramDataBase):
    pass

class TelegramData(TelegramDataBase):
    id: int
    class Config:
        orm_mode = True

# Object Detection Result Schemas
class DetectionResultBase(BaseModel):
    channel: str
    image_name: str
    x1: float
    y1: float
    x2: float
    y2: float
    confidence: float
    class_id: int
    class_name: str

class DetectionResultCreate(DetectionResultBase):
    pass

class DetectionResult(DetectionResultBase):
    id: int
    class Config:
        orm_mode = True
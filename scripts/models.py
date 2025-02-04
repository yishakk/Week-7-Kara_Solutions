from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from scripts.database import Base

class TelegramData(Base):
    __tablename__ = "cleaned_data"
    
    id = Column(Integer, primary_key=True, index=True)
    message_id = Column(DateTime)
    channel_title = Column(String)
    channel_username = Column(String)
    message = Column(Text)
    message_date = Column(DateTime)
    media_path = Column(String)

class ObjectDetectionResult(Base):
    __tablename__ = "object_detection_results"
    
    id = Column(Integer, primary_key=True, index=True)
    channel = Column(String)
    image_name = Column(String)
    x1 = Column(Float)
    y1 = Column(Float)
    x2 = Column(Float)
    y2 = Column(Float)
    confidence = Column(Float)
    class_id = Column(Integer)
    class_name = Column(String)
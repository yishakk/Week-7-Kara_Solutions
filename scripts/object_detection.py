import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from yolov5 import detect
import cv2
import torch
import logging
import pandas as pd
from sqlalchemy import create_engine

# Logging setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Paths
IMAGE_DIR = "data/photos"
OUTPUT_DIR = "data/processed/object_detection_results"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5m', force_reload=True)

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Database setup
DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URI)

def process_images(image_dir):
    detection_results = []
    for channel in os.listdir(image_dir):
        channel_dir = os.path.join(image_dir, channel)
        if not os.path.isdir(channel_dir):
            continue
        for image_name in os.listdir(channel_dir):
            image_path = os.path.join(channel_dir, image_name)
            logging.info(f"Processing image: {image_path}")

            # Run YOLO detection
            results = model(image_path)
            results.save(save_dir=OUTPUT_DIR)  # Save detection results

            # Extract detection data
            for detection in results.xyxy[0].numpy():
                x1, y1, x2, y2, confidence, class_id = detection
                detection_results.append({
                    'channel': channel,
                    'image_name': image_name,
                    'x1': x1,
                    'y1': y1,
                    'x2': x2,
                    'y2': y2,
                    'confidence': confidence,
                    'class_id': int(class_id),
                    'class_name': model.names[int(class_id)]
                })

    # Save results to a DataFrame
    df = pd.DataFrame(detection_results)
    return df

def save_to_database(df):
    try:
        df.to_sql('object_detection_results', engine, if_exists='replace', index=False)
        logging.info("Detection results saved to database.")
    except Exception as e:
        logging.error(f"Error saving to database: {e}")

if __name__ == "__main__":
    logging.info("Starting object detection process.")
    df = process_images(IMAGE_DIR)
    save_to_database(df)
    logging.info("Object detection completed successfully.")
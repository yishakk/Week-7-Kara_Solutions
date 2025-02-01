# **Ethiopian Medical Businesses Data Pipeline**

This project involves building a data pipeline to scrape, clean, transform, and analyze data from Ethiopian medical businesses sourced from Telegram channels and the web. The pipeline includes data scraping, cleaning, object detection using YOLO, and data warehouse implementation.

---

## **Project Overview**

### **Objectives**
1. **Data Scraping and Collection**:
   - Scrape data from Telegram channels and the web.
   - Collect text data and images for object detection.

2. **Data Cleaning and Transformation**:
   - Clean and standardize the scraped data.
   - Use DBT (Data Build Tool) for data transformation and testing.

3. **Object Detection**:
   - Use YOLO (You Only Look Once) for object detection on collected images.

4. **Data Warehouse Implementation**:
   - Design and implement a data warehouse for storing and analyzing the data.

5. **Data Integration and Enrichment**:
   - Integrate data from multiple sources and enrich it for deeper insights.

---

## **Project Structure**

```
ethiopian-medical-data-pipeline/
├── data/
│   ├── images/                  # Directory for scraped images
│   ├── raw/                     # Raw scraped data (JSON, CSV, etc.)
│   └── cleaned/                 # Cleaned and transformed data
├── scripts/
│   ├── telegram_scraper.py      # Script for scraping Telegram channels
│   ├── data_cleaning.py         # Script for data cleaning and transformation
│   └── object_detection.py      # Script for YOLO-based object detection
├── dbt/
│   ├── models/                  # DBT models for data transformation
│   ├── tests/                   # DBT tests for data validation
│   └── profiles.yml             # DBT configuration file
├── logs/                        # Logs for monitoring and debugging
├── README.md                    # Project documentation
└── requirements.txt             # Python dependencies
```

---

## **Setup Instructions**

### **Prerequisites**
1. **Python 3.8+**: Install Python from [python.org](https://www.python.org/).
2. **PostgreSQL**: Install PostgreSQL from [postgresql.org](https://www.postgresql.org/).
3. **DBT**: Install DBT using pip:
   ```bash
   pip install dbt
   ```
4. **Telethon**: Install the Telethon library for Telegram scraping:
   ```bash
   pip install telethon
   ```

### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ethiopian-medical-data-pipeline.git
   cd ethiopian-medical-data-pipeline
   ```
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the PostgreSQL database and update the connection details in `dbt/profiles.yml`.

---

## **Usage**

### **Task 1: Data Scraping and Collection**
1. Run the Telegram scraper script:
   ```bash
   python scripts/telegram_scraper.py
   ```
   - This script scrapes data from specified Telegram channels and stores it in `data/raw/telegram_raw_data.json`.
   - Images are saved in `data/images/{channel_name}/`.

2. Monitor logs in `logs/scraper.log`.

### **Task 2: Data Cleaning and Transformation**
1. Run the data cleaning script:
   ```bash
   python scripts/data_cleaning.py
   ```
   - This script cleans the raw data and stores it in `data/cleaned/cleaned_data.csv`.
   - Cleaned data is also loaded into the PostgreSQL database.

2. Use DBT for data transformation:
   ```bash
   cd dbt
   dbt run
   dbt test
   dbt docs generate
   dbt docs serve
   ```


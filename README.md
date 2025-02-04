# **Ethiopian Medical Businesses Data Warehouse**

![GitHub](https://img.shields.io/badge/License-MIT-blue) ![GitHub](https://img.shields.io/badge/Python-3.8%2B-green) ![GitHub](https://img.shields.io/badge/DBT-1.0%2B-orange) ![GitHub](https://img.shields.io/badge/YOLOv5-ultralytics-red)

This project is designed to build a **data warehouse** for Ethiopian medical businesses by scraping data from Telegram channels, cleaning and transforming the data, performing object detection using YOLO, and exposing the data via a **FastAPI** application. The goal is to provide actionable insights and enable data-driven decision-making for stakeholders.

---

## **Table of Contents**
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Project Structure](#project-structure)
6. [Technologies Used](#technologies-used)
7. [Contributing](#contributing)
8. [License](#license)
9. [Acknowledgements](#acknowledgements)

---

## **Project Overview**
The project involves the following key tasks:
1. **Data Scraping and Collection**: Scraping data from Telegram channels like `DoctorsET`, `Chemed`, and `lobelia4cosmetics` using the **Telethon** library.
2. **Data Cleaning and Transformation**: Cleaning and transforming the scraped data using **DBT (Data Build Tool)**.
3. **Object Detection**: Detecting objects in images from Telegram channels using **YOLOv5**.
4. **Data Warehouse Design**: Storing the processed data in a **PostgreSQL** database.
5. **API Exposure**: Exposing the data via a **FastAPI** application for easy access and querying.

---

## **Features**
- **Telegram Scraping**: Extract data from public Telegram channels using the Telethon library.
- **Data Cleaning**: Remove duplicates, handle missing values, and standardize data formats using DBT.
- **Object Detection**: Detect objects in images using YOLOv5 and store the results in a database.
- **Data Warehouse**: Store cleaned and transformed data in a PostgreSQL database.
- **FastAPI Integration**: Expose the data via a RESTful API for easy access and querying.

---

## **Installation**
Follow these steps to set up the project locally.

### **Prerequisites**
- Python 3.8+
- PostgreSQL
- Git

### **Steps**
1. Clone the repository:
   ```bash
   git clone https://github.com/teddyhabtamu/Kifiya-AIM-Week-7.git
   cd Kifiya-AIM-Week-7
   ```

2. Set up a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Set up the PostgreSQL database:
   - Create a database named `medical_data`.
   - Update the database connection details in `database.py`.

4. Install DBT and initialize the project:
   ```bash
   pip install dbt
   dbt init my_project
   ```

5. Set up YOLOv5:
   ```bash
   git clone https://github.com/ultralytics/yolov5.git
   cd yolov5
   pip install -r requirements.txt
   ```

---

## **Usage**
### **1. Data Scraping**
Run the Telegram scraping script:
```bash
python scripts/telegram_scraper.py
```

### **2. Data Cleaning and Transformation**
Run DBT transformations:
```bash
cd my_project
dbt run
dbt test
```

### **3. Object Detection**
Run YOLOv5 object detection on images:
```bash
python yolov5/detect.py --source path/to/images --weights yolov5s.pt --conf 0.25
```

### **4. FastAPI Application**
Start the FastAPI server:
```bash
uvicorn main:app --reload
```
Access the API at `http://localhost:8000`.

---
---

## **Technologies Used**
- **Python**: Primary programming language.
- **Telethon**: For scraping data from Telegram channels.
- **DBT**: For data transformation and cleaning.
- **YOLOv5**: For object detection in images.
- **PostgreSQL**: For data storage.
- **FastAPI**: For exposing data via a RESTful API.
- **SQLAlchemy**: For database interactions.
- **OpenCV**: For image processing.

---

## **Contributing**
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

---

## **License**
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## **Acknowledgements**
- [Telethon](https://docs.telethon.dev/) for Telegram scraping.
- [DBT](https://www.getdbt.com/) for data transformation.
- [YOLOv5](https://github.com/ultralytics/yolov5) for object detection.
- [FastAPI](https://fastapi.tiangolo.com/) for building the API.

---

For any questions or feedback, please open an issue or contact the project maintainer.

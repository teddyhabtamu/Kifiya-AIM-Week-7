from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Detection(Base):
    __tablename__ = "detections"

    id = Column(Integer, primary_key=True, index=True)
    image_path = Column(String, index=True)
    class_label = Column(String, index=True)
    confidence = Column(Float)
    bbox = Column(String)
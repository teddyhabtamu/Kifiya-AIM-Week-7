from pydantic import BaseModel

class DetectionBase(BaseModel):
    image_path: str
    class_label: str
    confidence: float
    bbox: str

class DetectionCreate(DetectionBase):
    pass

class Detection(DetectionBase):
    id: int

    class Config:
        orm_mode = True
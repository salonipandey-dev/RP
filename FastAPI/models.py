from pydantic import BaseModel
class TextInput(BaseModel):
    text: str 

class SeverityInput(BaseModel):
    text: str
    image_confidence: float
    
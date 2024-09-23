import numpy as np
import base64
from PIL import Image
import io

def sum(a, b):
    return a+b

def convert_jpg(image_data):
    image_bytes = base64.b64decode(image_data.split(",")[1])
    image = Image.open(io.BytesIO(image_bytes))
    image = image.convert("RGB")
    buffer = io.BytesIO()
    image.save(buffer, format="JPEG")
    jpg_image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return f"data:image/jpg;base64,{jpg_image_base64}"

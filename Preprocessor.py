# import cv2
import numpy as np
import base64
from PIL import Image
import io

def sum(a, b):
    return a+b

def sub(a, b):
    return a-b

def convert_jpg(image_data):
    image_bytes = base64.b64decode(image_data.split(",")[1])
    image = Image.open(io.BytesIO(image_bytes))
    
    # Convert image to RGB (in case it has an alpha channel)
    image = image.convert("RGB")
    
    # Create an in-memory buffer to store the image
    buffer = io.BytesIO()
    image.save(buffer, format="JPEG")
    
    # Encode the image in base64 and return as string
    jpg_image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return f"data:image/jpg;base64,{jpg_image_base64}"


# def convert_jpg(image_data):
#     header, base64_cdata = image_data.split(';base64,')
#     base64_data = base64_cdata.replace(' ','+')
#     img_data = base64.b64decode(base64_data)
#     np_array = np.frombuffer(img_data, np.uint8)
#     image = cv2.imdecode(np_array, cv2.IMREAD_UNCHANGED)
#     if image.shape[2] == 4:  # If image has an alpha channel
#         image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
#     elif image.shape[2] == 1:  # If image is grayscale
#         image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
#     success, encoded_image = cv2.imencode('.jpg', image, [int(cv2.IMWRITE_JPEG_QUALITY), 95])
   
#     if not success:
#         raise ValueError("Could not convert image to JPEG format.")

#     jpg_base64 = base64.b64encode(encoded_image).decode('utf-8')

#     return f"data:image/jpg;base64,{jpg_base64}"



import cv2
import numpy as np
import base64

def sum(a, b):
    return a+b

def sub(a, b):
    return a-b

def convert_jpg(image_data):
    header, base64_cdata = image_data.split(';base64,')
    base64_data = base64_cdata.replace(' ','+')
    img_data = base64.b64decode(base64_data)
    np_array = np.frombuffer(img_data, np.uint8)
    image = cv2.imdecode(np_array, cv2.IMREAD_UNCHANGED)
    if image.shape[2] == 4:  # If image has an alpha channel
        image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
    elif image.shape[2] == 1:  # If image is grayscale
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    success, encoded_image = cv2.imencode('.jpg', image, [int(cv2.IMWRITE_JPEG_QUALITY), 95])
   
    if not success:
        raise ValueError("Could not convert image to JPEG format.")

    jpg_base64 = base64.b64encode(encoded_image).decode('utf-8')

    return f"data:image/jpg;base64,{jpg_base64}"


# image_data = 'data:image/png;base64,...'  # Replace with your actual image data
# converted_image_data = convert_jpg(image_data)
# print(converted_image_data)

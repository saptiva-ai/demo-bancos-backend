import os
import numpy as np
import cv2
import pytesseract
from PIL import Image
from pdf2image import convert_from_path
from tempfile import NamedTemporaryFile

use_gpu = cv2.cuda.getCudaEnabledDeviceCount() > 0

def preprocess_image(image):
    image_cv = np.array(image)
    
    # Convertir a escala de grises
    if use_gpu:
        image_gpu = cv2.cuda_GpuMat(image_cv)
        gray_gpu = cv2.cuda.cvtColor(image_gpu, cv2.COLOR_BGR2GRAY)
        image_cv = gray_gpu.download()
    else:
        image_cv = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)

    # Convertir de nuevo a imagen PIL
    preprocessed_image = Image.fromarray(image_cv)
    
    return preprocessed_image

def ocr_pdf(file, doc_type):
    if file.content_type == "application/pdf":
        with NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
            temp_pdf.write(file.file.read())
            temp_pdf.flush()
            images = convert_from_path(temp_pdf.name, first_page=1, last_page=20)
        os.remove(temp_pdf.name)
    else:
        images = [Image.open(file.file)]

    text = ""
    for image in images:
        preprocessed_image = preprocess_image(image)
        text += pytesseract.image_to_string(preprocessed_image, lang='spa')
        print(text)
        text += "\n---\n"

    return text

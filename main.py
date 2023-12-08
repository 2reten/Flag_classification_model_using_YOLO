import os
import io
from flask import Flask, render_template, request
from PIL import Image
import base64
import logging
from ultralytics import YOLO
import glob
app = Flask(__name__)
from flask import send_from_directory
import time

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure 'uploads' folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

DETECT_FOLDER = 'runs/detect'
app.config['DETECT_FOLDER'] = DETECT_FOLDER

# Ensure 'runs/detect' folder exists
os.makedirs(DETECT_FOLDER, exist_ok=True)

@app.route("/")
def hello_world():
    return render_template('indexs.html')

@app.route('/detect', methods=['POST'])
def predict_img():
    if 'file' not in request.files:
        return render_template('indexs.html', error='No file part')

    file = request.files['file'] # 파일을 받아옴
    if file.filename == '':
        return render_template('indexs.html', error='No selected file')

    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        file_extension = file.filename.rsplit('.', 1)[1].lower()

        if file_extension == 'jpg':
            image = Image.open(filepath)
            yolo = YOLO('best_20_80_576.pt')
            detections = yolo.predict(image, save=True, save_dir=app.config['DETECT_FOLDER'])
            # Get the latest subfolder in 'runs/detect'

            subfolders = [f for f in os.listdir(app.config['DETECT_FOLDER']) if os.path.isdir(os.path.join(app.config['DETECT_FOLDER'], f))]
            latest_subfolder = max(subfolders, key=lambda x: os.path.getctime(os.path.join(app.config['DETECT_FOLDER'], x)))
            # Get the latest image in the latest subfolder
            latest_image_path = glob.glob(os.path.join(app.config['DETECT_FOLDER'], latest_subfolder, '*.jpg'))[0]
            # Encode the latest image to base64
            # print(latest_image_path)
            ori_img = image_to_base64(filepath)
            img_str = image_to_base64(latest_image_path)
            # 리턴할 데이터


            result = {
                'origin_image' : ori_img,
                'image': img_str,
                'objects': detections,
                'labels' : [detections[0].names[int(i)] for i in detections[0].boxes.cls], # 라벨 인식

            }

            return render_template('result.html', **result)

def image_to_base64(image_path):
    with open(image_path, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return f"data:image/jpeg;base64,{encoded_string}"




if __name__ == '__main__':
    app.run(debug=False)

# 웹 구현화

```python
import io
from IPython.display import display
import cv2
from flask import Flask, render_template, request,send_from_directory
from PIL import Image
import os
import base64

import torch
from ultralytics import YOLO
```

## 플라스크 앱 설정

```python
app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
```
-  Flask 웹 애플리케이션을 생성하고, 'uploads'라는 업로드 폴더를 설정한다

## 홈페이지 라우트
```python
@app.route("/")
def hello_world():
    return render_template('indexs.html')
```
- 라우트는 루트 URL에 접근했을 때 'indexs.html' 템플릿을 렌더링한다.

## 객체 검출 라우트

```python
def predict_img():
    if 'file' not in request.files:
        return render_template('indexs.html', error='No file part')

    file = request.files['file']
    if file.filename == '':
        return render_template('indexs.html', error='No selected file')

    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        file_extension = file.filename.rsplit('.', 1)[1].lower()

        if file_extension == 'jpg':
            image = Image.open(filepath)
            yolo = YOLO('best_20_80_576.pt')
            detections = yolo.predict(image, save=True)

            # 결과를 HTML 페이지에 표시할 수 있는 형식으로 변환
            results_html = ""
            for detection in detections:
                results_html += f"<p>{detection}</p>"

            # 이미지를 base64로 인코딩하여 HTML 페이지에 삽입
            img_str = image_to_base64(image)

            return render_template('result.html', image=img_str, results=results_html)
```

- '/detect' URL로 POST 요청이 들어오면 업로드된 이미지에서 객체 검출을 수행하고, 결과를 HTML 페이지에 표시한다.
    - 이미지는 'uploads' 폴더에 저장되고, YOLO 모델을 사용하여 객체 검출을 수행한다.
## 이미지를 Base64로 인코딩하는 함수

```python
def image_to_base64(image):
    # Convert the image to base64 format
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    img_str = "data:image/jpeg;base64," + base64.b64encode(buffered.getvalue()).decode()
    return img_str
```
- PIL을 사용하여 이미지를 JPEG 형식으로 변환하고, 그 결과를 Base64로 인코딩하여 HTML에 삽입할 수 있는 형식으로 반환한다.

## 디렉토리 및 파일 출력 함수
```python
def display(filename):
    # Display the latest generated image file in the 'runs/detect' directory
    folder_path = 'runs/detect'
    subfolders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]
    latest_subfolder = max(subfolders, key=lambda x: os.path.getctime(os.path.join(folder_path, x)))
    directory = folder_path + '/' + latest_subfolder
    print('printing directory:', directory)
    files = os.listdir(directory)
    latest_file = files[0]

    filename = os.path.join(folder_path, latest_subfolder, latest_file)
    file_extension = filename.rsplit('.', 1)[1].lower()
    environ = request.environ
    if file_extension == 'jpg':
        return send_from_directory(directory, latest_file, environ)
    else:
        return "invalid file format"
```
- 'runs/detect' 디렉토리에서 가장 최근에 생성된 이미지 파일을 출력하는 함수다.
    - 해당 파일은 Flask의 send_from_directory를 통해 웹 브라우저에 표시된다.
## Flask 애플리케이션 실행

```python
if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)
```
- 스크립트가 직접 실행될 때만 Flask 애플리케이션을 실행하며, 디버그 모드를 활성화한다.
# 두번째 프로젝트 시작

- 기간 : 11.27 ~ 12.8

- 머신러닝, 딥러닝을 이용해 모델 설계 후 웹으로 구현

```python
!pip install PyYAML
from google.colab import drive
drive.mount("/content/drive")
import yaml
import zipfile
with zipfile.ZipFile("/content/drive/MyDrive/flag_data_.zip") as target_file:
  target_file.extractall("/content/flag_data_")
data = {
    "train": "/content/flag_data_/flag_data_/train/images",
    "test": "/content/flag_data_/flag_data_/test/images",
    "val": "/content/flag_data_/flag_data_/valid/images",
    "names": ['china','deutsch','france','greatbritain', 'spain', 'england', 'hongkong', 'japan', 'korea', 'wales', 'nepal', 'norway', 'turkiye', 'USA', 'vietnam', 'argentina', 'belgium', 'brazil', 'canada', 'swiss', ],
    "nc":20
}
with open("/content/flag_data_/flag_data_/flag_data.yaml", "w") as f:
  yaml.dump(data, f)
with open("/content/flag_data_/flag_data_/flag_data.yaml", "r") as f:
  flag_yaml = yaml.safe_load(f)
  display(flag_yaml)
```

```python
pip install ultralytics
import ultralytics
from ultralytics import YOLO
```
```python
model = YOLO("yolov8n.pt")
model.train(data = "/content/flag_data_/flag_data_/flag_data.yaml", epochs = 10, patience = 5, batch = 32, imgsz = 416)
```

- 1일차는 주제를 정하는 것과 더불어 주로 데이터 라벨링에 힘을 쏟았다.
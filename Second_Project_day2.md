```python
import os

def flip_yolo_label(label_path, output_path):
    with open(label_path, 'r') as file:
        lines = file.readlines()

    flipped_labels = []

    for line in lines:
        values = line.strip().split()
        if len(values) == 5:
            class_id, x_center, y_center, width, height = map(float, values)

            # 좌우 반전
            flipped_x_center = 1.0 - x_center

            # 상하 반전
            #flipped_y_center = 1.0 - y_center

            flipped_labels.append([class_id, flipped_x_center, y_center, width, height])

    # 새로운 라벨 파일에 저장
    with open(output_path, 'w') as output_file:
        for label in flipped_labels:
            line = ' '.join(map(str, label))
            output_file.write(line + '\n')

def process_all_files(input_dir, output_dir):
    # 입력 디렉토리와 출력 디렉토리 확인
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 입력 디렉토리 내의 모든 라벨 파일 목록
    label_file_list = [file for file in os.listdir(input_dir) if file.endswith(".txt")]

    for label_file_name in label_file_list:
        # 라벨 파일의 경로
        label_path = os.path.join(input_dir, label_file_name)

        # 출력 라벨의 경로
        output_path = os.path.join(output_dir, label_file_name)

        # 라벨 변환
        flip_yolo_label(label_path, output_path)

# 예시 사용법
input_directory = '/content/flag_data_/flag_data_/train/labels/'
output_directory = '/content/flag_data_/flag_data_/train/output_directory'

process_all_files(input_directory, output_directory)
```
- 어제의 코드의 연장선이다.
    - yolo는 각 축의 최대값이 1이라 1에 축의 중심값을 빼면 반전되는 값이 나오는 것을 이용해 좌우반전을 시켜 그 데이터를 저장했다.

```python
import os

def flip_yolo_label(label_path, output_path):
    with open(label_path, 'r') as file:
        lines = file.readlines()

    flipped_labels = []

    for line in lines:
        values = line.strip().split()
        if len(values) == 5:
            class_id, x_center, y_center, width, height = map(float, values)

            # 상하 반전
            flipped_y_center = 1.0 - y_center

            flipped_labels.append([class_id, x_center,flipped_y_center, width, height])

    # 새로운 라벨 파일에 저장
    with open(output_path, 'w') as output_file:
        for label in flipped_labels:
            line = ' '.join(map(str, label))
            output_file.write(line + '\n')

def process_all_files(input_dir, output_dir):
    # 입력 디렉토리와 출력 디렉토리 확인
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 입력 디렉토리 내의 모든 라벨 파일 목록
    label_file_list = [file for file in os.listdir(input_dir) if file.endswith(".txt")]

    for label_file_name in label_file_list:
        # 라벨 파일의 경로
        label_path = os.path.join(input_dir, label_file_name)

        # 출력 라벨의 경로
        output_path = os.path.join(output_dir, label_file_name)

        # 라벨 변환
        flip_yolo_label(label_path, output_path)

# 예시 사용법
input_directory = '/content/flag_data_/flag_data_/train/labels/'
output_directory = '/content/flag_data_/flag_data_/train/output_directory'

process_all_files(input_directory, output_directory)
```

- 마찬가지로 상하 반전을 시키고 그 값을 저장하는 코드다.

```python
def flip_yolo_label(label_path, output_path):
    with open(label_path, 'r') as file:
        lines = file.readlines()

    flipped_labels = []

    for line in lines:
        values = line.strip().split()
        if len(values) == 5:
            class_id, x_center, y_center, width, height = map(float, values)

            # 상하 반전
            flipped_y_center = 1.0 - y_center

            flipped_labels.append([class_id, x_center, flipped_y_center, width, height])

    # 새로운 라벨 파일에 저장
    with open(output_path, 'w') as output_file:
        for label in flipped_labels:
            line = ' '.join(map(str, label))
            output_file.write(line + '\n')

def process_all_files(input_dir, output_dir):
    # 입력 디렉토리와 출력 디렉토리 확인
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 입력 디렉토리 내의 모든 라벨 파일 목록
    label_file_list = [file for file in os.listdir(input_dir) if file.endswith(".txt")]

    for label_file_name in label_file_list:
        # 라벨 파일의 경로
        label_path = os.path.join(input_dir, label_file_name)

        # 출력 라벨의 경로
        output_path = os.path.join(output_dir, label_file_name)

        # 라벨 변환
        flip_yolo_label(label_path, output_path)

# 예시 사용법
input_directory = '/content/flag_data_/flag_data_/train/labels/'
output_directory = '/content/flag_data_/flag_data_/train/output_labels_up_down'

process_all_files(input_directory, output_directory)
```
- 이 코드는 좌표값을 바꾸는 것을 이용해서 라벨링도 자동으로 완성시켰다.

```python
def flip_yolo_label(label_path, output_path):
    with open(label_path, 'r') as file:
        lines = file.readlines()

    flipped_labels = []

    for line in lines:
        values = line.strip().split()
        if len(values) == 5:
            class_id, x_center, y_center, width, height = map(float, values)

            # 좌우 반전
            flipped_x_center = 1.0 - x_center

            flipped_labels.append([class_id, flipped_x_center, y_center, width, height])

    # 새로운 라벨 파일에 저장
    with open(output_path, 'w') as output_file:
        for label in flipped_labels:
            line = ' '.join(map(str, label))
            output_file.write(line + '\n')

def process_all_files(input_dir, output_dir):
    # 입력 디렉토리와 출력 디렉토리 확인
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 입력 디렉토리 내의 모든 라벨 파일 목록
    label_file_list = [file for file in os.listdir(input_dir) if file.endswith(".txt")]

    for label_file_name in label_file_list:
        # 라벨 파일의 경로
        label_path = os.path.join(input_dir, label_file_name)

        # 출력 라벨의 경로
        output_path = os.path.join(output_dir, label_file_name)

        # 라벨 변환
        flip_yolo_label(label_path, output_path)

# 예시 사용법
input_directory = '/content/flag_data_/flag_data_/train/labels/'
output_directory = '/content/flag_data_/flag_data_/train/output_labels'

process_all_files(input_directory, output_directory)
```
- 이 코드는 좌우반전의 라벨링 코드다.
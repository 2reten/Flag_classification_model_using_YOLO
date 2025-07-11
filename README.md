# YOLO를 이용한 국기분류
<p align="center">
  <img src="https://github.com/2reten/ML-DL-Project/assets/145303952/123dc9f1-79df-4fac-a6dd-64b60ea19abc" width="350" height="350" alt="이미지">
</p>

## 프로젝트 소개

**Project Purpose**

 - This project aims to recognize images of national flags and output information about the translator's function and the country it represents.
 - 본 프로젝트는 국기의 이미지를 인식해 번역기의 기능과 해당 국가에 대한 정보를 출력하는 것을 목표로 하고 있습니다.
   
**Project Table of Contents**
- Collecting data
  - Decided that collecting flag image data for every country would be too time-consuming, so focused on 20 countries.
- Data labeling
  - Labeling each flag image to enable YOLO.
- Generate Data
  - In addition to the data we collected, we looked at the data and decided that it would not be difficult to distinguish the images when they were reversed upside down and left and right, so multiplied the images.
- Model design
  - Adjust the hyper-parameters of the YOLO model and compare the precision to improve the model's performance
- Implementing web page


<div align=center><h1>📚 STACKS</h1></div>

<div align=center>
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/CNN-CC0000?style=for-the-badge&logo=CNN&logoColor=white">
<img src="https://img.shields.io/badge/flask-000000?style=for-the-badge&logo=flask&logoColor=white">
<img src="https://img.shields.io/badge/jupyter-232F3E?style=for-the-badge&logo=jupyter&logoColor=white">
<img src="https://img.shields.io/badge/Pycharm-000000?style=for-the-badge&logo=pycharm&logoColor=white">
<img src="https://img.shields.io/badge/googlecolab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white">
<br>
</div>

## 프로젝트 목표 및 동기
**Project goals and motivation**
- This project develops an object detection model that utilizes YOLO to classify national flags. It effectively identifies flags used in various multicultural communities to highlight cultural diversity and promote mutual understanding in a multicultural society. To improve the accuracy of the model, we go through steps such as data collection, labeling, and data multiplication, aiming to detect accurate objects for each flag. We also visualize the model through a web page, allowing users to check and interact with the model's predictions for various flags. This contributes to highlighting cultural diversity and promoting mutual understanding in a multicultural society.

- 이 프로젝트는 YOLO를 활용하여 국기를 분류하는 객체 감지 모델을 개발합니다. 다양한 다문화 커뮤니티에서 사용되는 국기를 효과적으로 식별하여 문화 다양성을 강조하고 다문화 사회에서 상호이해를 촉진합니다. 모델의 정확성 향상을 위해 데이터 수집, 라벨링, 데이터 증식 등의 단계를 거치며, 각 국기에 대한 정확한 객체 감지를 목표로 합니다. 또한, 웹 페이지를 통해 모델을 시각화하여 사용자들이 다양한 국기에 대한 모델의 예측을 확인하고 상호작용할 수 있도록 합니다. 이를 통해 문화적 다양성을 강조하고 다문화 사회에서의 상호이해를 촉진하는 데 기여합니다.
  
## 프로젝트 진행 과정
**Project progression**

- Data labeling process
  
 ![ezgif-3-5c127d029d-ezgif com-video-to-gif-converter](https://github.com/2reten/ML-DL-Project/assets/145303952/6b392ffb-fc57-47f5-86df-e263dfb3a8e6)

- Final result
  
![unnamed (2)](https://github.com/2reten/ML-DL-Project/assets/145303952/522d172f-93fb-40d4-82c0-53ffc825e29a)

![unnamed (1)](https://github.com/2reten/ML-DL-Project/assets/145303952/cd60ca21-b3b6-4fd8-b2e8-df20e41c630b)




## 문제점과 한계
**Issues and limitations**
- The main problem we faced during the project was not only the performance of the model, but also its accuracy. If a model is only adapted to a specific background, its performance in classifying flags in other environments can be compromised. If it relies too heavily on the features of a specific environment, it can have difficulty classifying flags in less common backgrounds. Furthermore, flags can come in different sizes and proportions. If your model is only adapted to a specific size, it may have difficulty recognizing flags of different sizes correctly. To reduce sensitivity to size variations, it is necessary to utilize data augmentation techniques or train the model by incorporating images of flags of different sizes.
  
- 프로젝트를 수행하면서 마주한 주요 문제점은 모델의 성능 뿐만이 아닌 정확도 역시도 뛰어나지 않다는 것이었습니다. 모델이 특정 배경에만 적응되어 있으면, 다른 환경에서의 국기 분류 성능이 저하될 수 있습니다. 특정 환경의 특징에 지나치게 의존하면, 일반적이지 않은 배경에서 국기를 제대로 분류하기 어려울 수 있습니다. 뿐만 아니라, 국기는 다양한 크기와 비율로 존재할 수 있습니다. 모델이 특정 크기에만 적응되어 있다면, 다양한 크기의 국기를 올바르게 인식하기 어려울 수 있습니다. 크기 변형에 대한 민감성을 감소시키기 위해서는 데이터 증식 기법을 활용하거나, 다양한 크기의 국기 이미지를 통합하여 모델을 학습시키는 것이 필요합니다.

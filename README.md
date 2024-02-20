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
<img src="https://img.shields.io/badge/selenium-4FC08D?style=for-the-badge&logo=selenium&logoColor=white">
<img src="https://img.shields.io/badge/plotly-000000?style=for-the-badge&logo=plotly&logoColor=white">
<img src="https://img.shields.io/badge/jupyter-232F3E?style=for-the-badge&logo=jupyter&logoColor=white">
<img src="https://img.shields.io/badge/pandas-F05032?style=for-the-badge&logo=pandas&logoColor=white">
<br>
</div>

## 프로젝트 목표 및 동기
**Project goals and motivation**
- The main goal of this project is to understand and analyze the political leanings of various media outlets on the issue of contaminated water discharge from the Fukushima nuclear power plant. As the media's approach to environmental issues has a great impact on shaping social consciousness and public debate, we hope to gain insight into the interaction between political positions and the media by understanding how each media outlet is reacting to this issue. In addition, this project aims to contribute to international comparative media research by conducting accurate sentiment analysis taking into account language differences and cultural characteristics.

- 이 프로젝트의 주된 목표는 후쿠시마 원전에서 발생한 오염수 방류 문제에 대한 다양한 언론사들의 정치적 성향을 이해하고 분석하는 것입니다. 환경 문제에 대한 언론의 접근 방식은 사회적 의식을 형성하고 공론화하는 데 큰 영향을 미치기 때문에, 각 언론사가 이 문제에 어떻게 반응하고 있는지를 파악함으로써 정치적 입장과 언론의 상호작용에 대한 통찰을 얻고자 합니다. 또한, 이 프로젝트는 언어 간의 차이와 문화적 특성을 고려하여 정확한 감정 분석을 수행함으로써 국제적인 언론 비교 연구에 기여하고자 합니다.

## 프로젝트 진행 과정
**Project progression**

- Crawling process
  
![ezgif com-crop](https://github.com/2reten/Vis_Project/assets/145303952/7f1f8978-8140-4c8f-b1f2-7b2aa4fe5f89)

- Final result
<div>
  <a href="https://plotly.com/~2reten/20/" target="_blank">
    <img src="https://plotly.com/~2reten/20.png" alt="Interactive Chart"/>
  </a>
</div>


## 문제점과 한계
**Issues and limitations**
- The main problem we encountered during the project was the difficulty in accurately conveying contextual differences between languages. Failure to account for the variations in vocabulary and expression that occur during translation can compromise the accuracy of sentiment analysis. In addition, current sentiment analysis algorithms may not take into account the importance of certain vocabulary because they weight each word in bulk. This can make it difficult to accurately determine the topics or tone that a particular journalist is emphasizing. In future research, we hope to overcome these issues by introducing more sophisticated models that better understand context and weight sentiment analysis.
  
- 프로젝트를 수행하면서 마주한 주요 문제점은 언어 간의 문맥 차이를 정확하게 전달하기 어렵다는 것입니다. 번역 과정에서 발생하는 어휘와 표현의 다양성을 고려하지 못하면 감정 분석의 정확성이 저하될 수 있습니다. 또한, 현재의 감정 분석 알고리즘은 각 단어의 가중치를 일괄적으로 적용하므로 특정 어휘의 중요성을 고려하지 못할 수 있습니다. 이로 인해 특정 언론사가 강조하는 주제나 어조를 정확하게 파악하기 어려울 수 있습니다. 향후 연구에서는 문맥을 보다 잘 이해하고 감정 분석에 가중치를 부여하는 더 정교한 모델을 도입하여 이러한 문제를 극복하고자 합니다.

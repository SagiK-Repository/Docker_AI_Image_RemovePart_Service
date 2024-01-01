문서정보 : 2023.12.19.~ 작성, 작성자 [@SAgiKPJH](https://github.com/SAgiKPJH)

<br>

# Docker_AI_Image_RemovePart_Service
이미지 일부분 제거, 도커를 활용한 웹사이트 활용 프로그램

### 목표
- [ ] 이미지 지우기 AI 탐색
- [x] Web VSCode Jupyter Image Mask Drawing
- [x] 독립적인 Docker Python 환경에서 LaMa 구동 Test

### 제작자
[@SAgiKPJH](https://github.com/SAgiKPJH)

<br>
---
<br>

### 이미지 지우기 AI 탐색과정 (https://github.com/SagiK-Repository/Docker_AI_Image_RemovePart_Service/issues/1)

<br>

### Web VSCode Jupyter Image Mask Drawing (https://github.com/SagiK-Repository/Docker_AI_Image_RemovePart_Service/issues/4)
<img src="https://github.com/SagiK-Repository/Docker_AI_Image_RemovePart_Service/assets/66783849/f926b56a-1e32-4519-a533-f15684f270ad" width=50%/>

<br>

### 독립적인 Docker Python 환경에서 LaMa 구동 Test (https://github.com/SagiK-Repository/Docker_AI_Image_RemovePart_Service/issues/2)

<img src="https://github.com/SagiK-Repository/Docker_AI_Image_RemovePart_Service/assets/66783849/dc893c82-6fa0-4a25-95cd-a85106e7912d" width=50%/>  

- 빠른 시작
  ```bash
  docker run -it --gpus all --name vscode-container -p 18087:8080 juhyung1021/docker-vscode-python_lama:1.0-cpu

  # or
  
  nvidia-docker run -it -p 18087:8080 -d juhyung1021/docker-vscode-python_lama:1.0-cpu
  ```
- 이후 브라우저를 통해 `127.0.0.1:18087`로 이동 후 Login 합니다.  
  - ID : user  
  - Password : password  

<img src="https://github.com/SagiK-Repository/Docker_AI_Image_RemovePart_Service/assets/66783849/12774562-53f7-47f8-b890-84a24a7616bd"/>

📽️Video▶️ [<img src="https://github.com/SagiK-Repository/Docker_AI_Image_RemovePart_Service/assets/66783849/43e76597-7052-4c04-b89e-44aea033aae6"/>](https://www.youtube.com/watch?v=WuArNdlpcgM)

<br>

### GPU 활용한 LaMa 구동 (https://github.com/SagiK-Repository/Docker_AI_Image_RemovePart_Service/issues/5)

-빠른 시작
  - 환경 제공
  ```bash
  docker run -it --gpus all --name vscode-container -p 18087:8080 juhyung1021/docker-vscode-python_lama:11.1-gpu
  
  # or
  
  nvidia-docker run -it -p 18087:8080 -d juhyung1021/docker-vscode-python_lama:11.1-gpu
  ```
  - 필요 파일(image, jupyter file) setting 된 image
  ```bash
  docker run -it --gpus all --name vscode-container -p 18087:8080 juhyung1021/docker-vscode-python_lama:set-11.1-gpu
  
  # or
  
  nvidia-docker run -it -p 18087:8080 -d juhyung1021/docker-vscode-python_lama:set-11.1-gpu
  ```

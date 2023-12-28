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

<img src="https://private-user-images.githubusercontent.com/66783849/293121219-eef72bf2-0912-4027-950c-610e3a91d4ea.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDM3Mjg0MTIsIm5iZiI6MTcwMzcyODExMiwicGF0aCI6Ii82Njc4Mzg0OS8yOTMxMjEyMTktZWVmNzJiZjItMDkxMi00MDI3LTk1MGMtNjEwZTNhOTFkNGVhLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzEyMjglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMjI4VDAxNDgzMlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTkxNmIzZTRlOGYzMjI5NGUwNjA5ZTVkNjcxNTM4NjkzODQ2ZWM3MDEzN2MyMDlmNDI4MTU3OTk4ZDkzYjY4OTYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.ma-hIUDC3pFqIL_30oXP91p6TdsgHrPFSOI_cbJ8qvw" width=50%/>  

- 빠른 시작
  ```bash
  docker run -it --gpus all --name vscode-container -p 18087:8080 juhyung1021/docker-vscode-python_lama:1.0-cpu
  ```
- 이후 브라우저를 통해 `127.0.0.1:18087`로 이동 후 Login 합니다.  
  - ID : user  
  - Password : password  

<img src="https://private-user-images.githubusercontent.com/66783849/293118293-865b7b72-de3a-46e9-9f63-acf768640acf.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDM3MjY1NDAsIm5iZiI6MTcwMzcyNjI0MCwicGF0aCI6Ii82Njc4Mzg0OS8yOTMxMTgyOTMtODY1YjdiNzItZGUzYS00NmU5LTlmNjMtYWNmNzY4NjQwYWNmLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzEyMjglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMjI4VDAxMTcyMFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPThkMWEzMWYyYzY5YTdiNzJjYTIwMzU0Mjk0OTBiZmRkNWQzNTE3NzQyNjQzYzU1NzFlMzY0NDM0ODNhMGQ4MzYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.69y3hs2Cx12nDsnDkRCKY_S6p1QlmcwjMdM27bGV_Fo"/>

📽️Video▶️ [<img src="https://github.com/SagiK-Repository/Docker_AI_Image_RemovePart_Service/assets/66783849/43e76597-7052-4c04-b89e-44aea033aae6"/>](https://www.youtube.com/watch?v=WuArNdlpcgM)



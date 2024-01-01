from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import base64
from PIL import Image
import io
import subprocess

app = Flask(__name__)
CORS(app) # 클라이언트로부터의 요청에 대해 모든 도메인에서 접근 허용(CORS 허용)

def inaryImageToImage(image_data):
    # base64 디코딩하여 이미지 바이너리 데이터 추출
    image_binary = base64.b64decode(image_data.split(',')[1])

    # 바이너리 데이터를 Pillow(PIL) Image 객체로 변환
    image = Image.open(io.BytesIO(image_binary))

    return image

@app.route('/', methods=['GET'])
def index():
    return "Hello, World!"

@app.route('/uploadImage', methods=['POST'])
def uploadImage():
    print("uploadImage")
    # 이미지 데이터 받아오기 (JSON 형태)
    image_data_json=request.get_json()
    image_data = image_data_json['image_data']

    image = inaryImageToImage(image_data)

    image.save('./image/image.png')

    return ""

@app.route('/running', methods=['POST'])
def running():
    print("running")
    # 이미지 데이터 받아오기 (JSON 형태)
    image_data_json=request.get_json()
    image_data = image_data_json['image_data']

    image = inaryImageToImage(image_data)

    image.save('./image_mask.png')

    return jsonify({'prediction': int(0)})

if __name__ == '__main__':
	app.run(host='0.0.0.0') # 포트 외부 접근 허용
     
def runLaMa() :
    # nvidia-smi 명령어 실행
    result = subprocess.run(['PYTHONPATH=./lama TORCH_HOME=./lama python3 ./lama/bin/predict.py model.path=./big-lama indir=/var/www/html/image outdir=/var/www/html/outdir dataset.img_suffix=.png > /dev/null'], capture_output=True, text=True)
    
    # 실행 결과 출력
    output = result.stdout
    print(output)
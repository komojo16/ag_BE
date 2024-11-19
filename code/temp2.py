import eventlet
eventlet.monkey_patch()

import os
from flask import Flask, send_from_directory, jsonify, request
import qrcode


# QR 코드 생성 함수
def generate_qr_code_with_download_link():
    # QR 코드 데이터: 파일 다운로드 URL 생성
    download_url = f"http://192.168.1.26:8888/download/res.png"

    # QR 코드 생성
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(download_url)
    qr.make(fit=True)

    # QR 코드 이미지를 저장
    qr_image_path = os.path.join(r"C:\Users\kyle0\Desktop\ag_BE\res_img", "qr_code.png")
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(qr_image_path)
    return qr_image_path




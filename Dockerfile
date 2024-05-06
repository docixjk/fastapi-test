# Docker 이미지의 베이스를 정의
FROM python:3.9

# 컨테이너 내에서 작업 디렉토리를 설정
WORKDIR /app

# requirements.txt를 작업 디렉토리로 복사
COPY requirements.txt /app/

# pip를 사용하여 requirements.txt 파일에 명시된 Python 종속성을 설치
RUN pip install --no-cache-dir -r requirements.txt

# 현재 디렉토리의 모든 파일을 컨테이너 내부의 /app 디렉토리로 복사
COPY . /app

# Uvicorn을 사용하여 FastAPI 애플리케이션을 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

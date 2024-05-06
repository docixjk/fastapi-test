# 사용할 기본 이미지를 지정합니다.
FROM python:3.9

# 작업 디렉토리를 설정합니다.
WORKDIR /app

# 프로젝트의 의존성을 설치합니다.
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# app 폴더의 파일을 컨테이너의 /app 디렉토리로 복사합니다.
COPY ./app /app

# Uvicorn 서버를 실행합니다.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

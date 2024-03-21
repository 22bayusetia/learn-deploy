# Dockerfile
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./model.pkl /app/model.pkl
COPY ./app.py /app/app.py

RUN pip install joblib scikit-learn

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]

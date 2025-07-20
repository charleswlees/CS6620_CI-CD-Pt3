FROM python:3.11-alpine

COPY api.py db.py requirements.txt ./
COPY services/ ./services/

RUN apk add --no-cache curl
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python", "api.py"]







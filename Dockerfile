FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt \
    && apt-get update \
    && apt-get install -y locales \
    && apt-get install -y ffmpeg \
    && useradd -m appuser \
    && chown -R appuser /app

ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV LANG=ar_SA.UTF-8
ENV LANGUAGE=ar_SA:ar
ENV LC_ALL=ar_SA.UTF-8

RUN locale-gen ar_SA.UTF-8

USER appuser

EXPOSE 8080

CMD ["python", "transcribe.py"]
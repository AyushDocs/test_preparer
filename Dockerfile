FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

ENV   PYTHONUNBUFFERED=1 \
      STREAMLIT_SERVER_PORT=8501 \
      STREAMLIT_SERVER_ADDRESS=0.0.0.0

ARG OPENAI_API_KEY, LANGCHAIN_API_KEY

ENV OPENAI_API_KEY=${OPENAI_API_KEY} \
    LANGCHAIN_API_KEY=${LANGCHAIN_API_KEY}

CMD ["streamlit", "run", "app.py"]

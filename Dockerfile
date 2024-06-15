FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade --no-cache-dir setuptools
RUN pip3 install --no-cache-dir -r requirements.txt && chmod 755 .
COPY . .

RUN pip install -r requirenemts.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
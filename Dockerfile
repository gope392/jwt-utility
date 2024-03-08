FROM python:3.10-alpine

# Prevent Python from write bytecode & send output straight to terminal
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /jwt-utility

COPY requirements.txt /jwt-utility/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /jwt-utility/

CMD ["python3", "./src/jwtutil.py"]

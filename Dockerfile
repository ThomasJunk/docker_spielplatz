FROM python:3.7-alpine

ARG MSG="Hello"
WORKDIR /code
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN echo "${MSG}"
COPY . .
CMD ["python", "server.py"]
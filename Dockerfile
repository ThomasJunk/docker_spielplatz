FROM python:3.7-alpine

ARG REPOSITORY="https://github.com/ThomasJunk/docker_spielplatz"
ARG COMMIT=master
WORKDIR /code
RUN apk add --no-cache gcc musl-dev linux-headers git \
    && addgroup -S appgroup \
    && adduser -S appuser -G appgroup \
    && git clone --no-checkout -- $REPOSITORY . \
    && git checkout $COMMIT \
    && pip install -r requirements.txt \
    && chown -R appuser:appgroup /code
USER appuser
ENV PORT=8000
CMD ["python", "server.py"]
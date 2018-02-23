FROM python:alpine3.7

RUN echo \
  && pip install asyncio aiosmtpd \
  && echo

EXPOSE 8025

WORKDIR /app
ADD server.py /app/server.py
CMD ["python", "/app/server.py"] 
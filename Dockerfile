FROM python:alpine3.8
ARG GITHASH
ENV HASH=$GITHASH
ENV COLOR=RED
ENV APP_NAME=SplitCamelCase
COPY app.py /app/app.py
COPY versionz.py /app/versionz.py
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
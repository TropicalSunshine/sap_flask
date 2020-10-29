FROM ubuntu:16.04
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT [ "python" ]
CMD [ "server.py"]
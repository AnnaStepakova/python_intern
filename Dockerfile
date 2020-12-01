FROM python:3.9
WORKDIR /python_intern
ADD app.py ./
ADD requirements.txt ./
RUN pip install -r requirements.txt
EXPOSE 8000
CMD python ./app.py
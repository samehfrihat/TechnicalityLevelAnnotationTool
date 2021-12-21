FROM python:3.10

ENV PYTHONPATH=.

WORKDIR .

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 8787

CMD python3 src/run.py
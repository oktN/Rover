FROM python:3.6.6

ENV PYTHONPATH /opt/kata/

RUN pip install pipenv

WORKDIR $PYTHONPATH
COPY Pipfile* .
RUN pipenv install --dev

COPY . .

CMD ["pipenv", "run", "mamba", "--format=documentation"]

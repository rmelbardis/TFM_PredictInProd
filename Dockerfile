
# write some code to build your image

# FROM
FROM python:3.8.12-buster

# COPY
COPY model.joblib /model.joblib
COPY api /api
COPY TaxiFareModel /TaxiFareModel
COPY requirements.txt /requirements.txt

# RUN
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# CMD
CMD uvicorn api.fast:app --host 0.0.0.0

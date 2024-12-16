FROM python:3.12
WORKDIR /code
COPY python_frontend/project/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY python_frontend/project/frontend.py /code/
CMD ["python", "frontend.py"]
ENTRYPOINT ["python","frontend.py"]
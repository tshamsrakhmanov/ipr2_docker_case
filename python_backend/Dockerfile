FROM python:3.12
WORKDIR /code
COPY python_backend/project/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY python_backend/project/backend.py /code/
CMD ["python", "backend.py"]
ENTRYPOINT ["python","backend.py"]
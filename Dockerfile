FROM python:3.7-slim
COPY ./ /app
RUN pip install -r /app/requirements.txt
WORKDIR /app/right_hand/
CMD python manage.py runserver 0:5000
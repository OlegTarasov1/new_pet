FROM python

COPY ./notion_like_app /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip -r requirements.txt

COPY . /app/

COPY ./entrypoint.sh /app/entrypoint.sh

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT [ "/app/entrypoint.sh" ]

CMD ["gunicorn", "todo_list.wsgi:application", "--bind", "0.0.0.0:8000"]

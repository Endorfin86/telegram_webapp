FROM python:3.8
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 4000
COPY ./ /app
CMD [ "python", "bot.py" ]
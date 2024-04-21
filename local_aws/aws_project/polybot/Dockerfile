FROM python
WORKDIR /app
RUN pip install --upgrade pip
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8443
CMD ["python3", "app.py"]

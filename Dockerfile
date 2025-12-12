FROM python:3.10
# Install Tkinter dependencies and other needed packages
RUN apt-get update && apt-get install -y 
WORKDIR /app
COPY . .
# Install Python dependencies (if any)
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
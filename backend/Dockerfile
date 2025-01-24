FROM python:3.10

# Set working directory
WORKDIR /app

# Install dependencies
COPY backend/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY backend /app

# Set the environment variable for Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# Expose port for Flask
EXPOSE 5000

# Run the app
CMD ["flask", "run", "--host", "0.0.0.0"]

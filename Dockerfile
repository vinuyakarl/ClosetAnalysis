FROM python:3.13
WORKDIR /usr/local/app

# Install the app dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy Alembic config and migration scripts
COPY alembic.ini .
COPY alembic ./alembic

# Copy the scripts
COPY scripts ./scripts

# Copy in the source code
COPY src .
EXPOSE 8080

# Setup an app user so the container doesn't run as the root user
RUN useradd app
USER app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
# Pull python 3 image
FROM python:3
# Create a work dir
WORKDIR /app
# copy requirements.txt into workdir created above
COPY requirements.txt /app
# Install all requirements
RUN python3 -m pip install --user --no-cache-dir -r requirements.txt
# Copy entire project into workdir
COPY app.py /app
# Run our app without output
CMD ["python", "/app/app.py"]
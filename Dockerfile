FROM arm64v8/python:3.11-bookworm

WORKDIR /app

# Install RPi.GPIO  and any needed packages specified in requirements.txt
# COPY requirements.txt ./
RUN pip install --no-cache-dir st7036 sn3218==1.2.7 smbus psutil
RUN pip install --no-cache-dir dot3k
RUN pip uninstall -y rpi.gpio && pip3 install --no-cache-dir rpi-lgpio

COPY app.py graph.py clock.py cpu.py ./

CMD ["python3", "/app/app.py"]
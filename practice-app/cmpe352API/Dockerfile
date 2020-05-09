FROM python:3
# set the working directory of the app
WORKDIR /usr/src/app
# copy the files to the container
COPY . .
# install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# the port number to expose
EXPOSE 5000
# run python with ./app.py
CMD ["python", "./app.py"]

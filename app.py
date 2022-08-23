from flask import Flask
import sys
from housing.logger import logging
from housing.exception import HousingException
app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        housing=HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info("First logging")
    return "Hello, This is example for CICD pipeline"





if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
import requests

app = Flask(__name__)
api = Api(app)

Class Address(self)

    def __init__(self):
    
        self.my_headers = {'Authorization' : 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjExNyIsImNvbnN1bWVyTmFtZSI6IkludGVydmlld3MiLCJjb25zdW1lclR5cGUiOiIxIiwibmJmIjoxNjE5Nzc1NTY2LCJleHAiOjE5MzUzMDgzNjYsImlhdCI6MTYxOTc3NTU2Nn0.OIbvEbkNecLDOky7bI_fi1r6yxgLxwcFAvy6hbvKpTY'}
        self.response = requests.get("https://6kb2p9kgb0.execute-api.eu-west-2.amazonaws.com/production/api/v1/addresses/?postcode="+, headers=my_headers)
        

    def get(self)
        response




api.add_resource(Address, '/address')  # add endpoint

if __name__ == '__main__':
    app.run()

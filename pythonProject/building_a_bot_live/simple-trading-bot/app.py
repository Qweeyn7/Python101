import datetime
import json

import boto3
import requests
from chalice import Chalice
from credentials.config import *

s3 = boto3.resource('s3')

app = Chalice(app_name='simple-trading-bot')
ONADA_API_URL = "https://api-fxpractice.oanda.com"




@app.route('/what-time-is-it')
def get_time():
    return {"message": "The Time Right Now is: " + str(datetime.datetime.now())}


@app.route('/create_order')
def create_order():
    try:
        payload = {
            "order": {
                "units": "300",
                "instrument": "EUR_USD",
                "timeInForce": "FOK",
                "type": "MARKET",
                "positionFill": "DEFAULT"
            }
        }

        ORDERS_URL = "{}/v3/accounts/{}/orders".format(ONADA_API_URL, ACCOUNT_ID)
        HEADERS = {'Authorization': "Bearer " + ACCESS_TOKEN, 'Content-Type': "application/json"}

        r = requests.post(ORDERS_URL, json=payload, headers=HEADERS)
        order_status = json.loads(r.content)
        print(order_status)
        return order_status

    except Exception as e:
        return str(e)


@app.route('/view_orders')
def view_order():
    pass


@app.route('/stop_orders')
def stop_order():
    pass



# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#

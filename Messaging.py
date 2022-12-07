import os
from twilio.rest import Client

class SMS:

    account_sid = os.environ['AC1385351c76f52c0899c297a8be387a32']
    auth_token = os.environ['955b53aec92b587c2c2bfbc466ecf80f']
    client = Client(account_sid, auth_token)

    def scheduled_message()
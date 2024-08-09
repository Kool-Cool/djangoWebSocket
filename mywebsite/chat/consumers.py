#channels version of view 
# response to  request from client and initate while keeping open 

import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({
            'type': 'connection_established',
            'message': 'You are now Connected!',
        }))


    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        print("Message from WEB" , message)

        self.send(text_data = json.dumps({
            "type": "chat",
            "message" : message ,
        }))




    # def disconnect(self, close_code):
    #     pass


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

    # Uncomment and implement these methods if needed
    # def receive(self, text_data):
    #     pass

    # def disconnect(self, close_code):
    #     pass


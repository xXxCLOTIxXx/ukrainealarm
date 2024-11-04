import websocket
import json
from threading import Thread
from .utils.headers import get_ws_headers


#TODO
class Socket:
    def __init__(self, centrifugo_url, api_token, centrifugo_token):
        self.centrifugo_url = centrifugo_url
        self.api_token = api_token
        self.centrifugo_token = centrifugo_token
        self.is_connected = False
        self.ws = None

    def on_message(self, ws, message):
        print("Получено сообщение:", message)

    def on_error(self, ws, error):
        print("Ошибка WebSocket:", error)

    def on_close(self, ws, close_status_code, close_msg):
        print("Соединение закрыто")
        self.is_connected = False

    def on_open(self, ws):
        print("Соединение установлено")
        self.is_connected = True
        ws.send(json.dumps({"event": "connect"}))


	#--------------------------------
    
	#TODO
    def connect(self, threading: bool = True):
        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(
            self.centrifugo_url,
            header=get_ws_headers(),
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        Thread(target=self.ws.run_forever).start() if threading else self.ws.run_forever()


    def send_message(self, message):
        if self.ws and self.is_connected:
            self.ws.send(json.dumps(message))
            print("Отправлено сообщение:", message)

    def close(self):
        if self.ws:
            self.ws.close()

	#TODO
    def refresh_token(self):
        url = f"{self.centrifugo_url}/api/centrifuge/refreshToken"
        return url

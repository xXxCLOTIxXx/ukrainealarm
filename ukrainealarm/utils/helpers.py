from bs4 import BeautifulSoup



def get_info_from_basic_html(content: str):

    soup = BeautifulSoup(content, "html.parser")
    api_token = soup.find("input", {"id": "api-token"})["value"]
    centrifugo_token = soup.find("input", {"id": "centrifugo-token"})["value"]
    centrifugo_url = soup.find("input", {"id": "centrifugo-url"})["value"]

    return {
        "api_token": api_token,
        "websocket_token": centrifugo_token,
        "websocket_url": centrifugo_url
    }
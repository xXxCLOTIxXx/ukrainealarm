


def get_headers(cookie: str, user_agent: str = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0", token: str = None, content_type: str = None):
    h = {
        "Cookie": cookie,
        #"Host": "map.ukrainealarm.com",
        "User-Agent": user_agent
    }
    
    if content_type:
        h["Content-Type"] = content_type
    if token:
       h["Authorization"] = "Bearer " + token

    return h


def get_ws_headers():
    headers = {
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
                "Cache-Control": "no-cache",
                "Connection": "keep-alive, Upgrade",
                "Cookie": "_ga_9QLR0Q6YVH=GS1.1.1730742296.5.1.1730742311.0.0.0; _ga=GA1.1.14244204.1730724902; cf_clearance=8fybng.4f7tiykJg9kPHJwukQr0GaAsCQNdvNqKayLg-1730742295-1.2.1.1-Kk7prQeXua6.nM6ybA6bf96CiwqcL3Dzm_xQu0wbwYnZ84Kc6ziYB14AlNz3RcS6NQ5z10egT87oeb56S4C1rs6cKSDL2qK.OTrD3JL6nJ1AgvqtkOnMmJbRmtkTT8jBrq9Z8.PiwN1EBmFSvUGW7tHB_.qj7UxMCeR1lvQX9WA4X2n0rwOpQGUMouSXRxbbw_tHF3AwWxVv763Lvjmn8PI_eW5HrrorXXbBH8HBLYIsJs92iehZ6kWxosGxT2BXsJrPPjLpuHidlVvlRLLFz8L.FgzLTqhgCHXatsL.CgYsFJoLzRSeicuQ5sG5isSfYR9wy.fq9f0Co05_Ipb2FmLpEW5QB57HNY4XMOuUVXiRgyjyx2s_Bbaw3Zpvf27ylG2dtbSCn09b_HZWXi56fA",
                "Host": "ws.ukrainealarm.com",
                "Origin": "https://map.ukrainealarm.com",
                "Pragma": "no-cache",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "websocket",
                "Sec-Fetch-Site": "same-site",
                "Sec-WebSocket-Extensions": "permessage-deflate",
                "Sec-WebSocket-Key": "rb+G+QpmgNO4hJYyObP0tQ==",
                "Sec-WebSocket-Version": "13",
                "Upgrade": "websocket",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0"
            }
    
    return headers
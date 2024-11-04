import cloudscraper
from .utils.headers import get_headers
from .utils.req import requester
from .utils.helpers import get_info_from_basic_html
from .utils.exceptions import CheckException
from .socket import Socket

class Client:
    url: str = "https://map.ukrainealarm.com/"
    scraper = cloudscraper.create_scraper()
    

    def __init__(self, user_agent: str = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0", cf_token: str = None):
        self.req = requester(
            auth_data=get_info_from_basic_html(
                self.get_basic_html(
                    user_agent, cf_token
                )
            ),
            user_agent=user_agent, cookie=cf_token
        )
        #TODO SOCKET
        """        
        self.socket = Socket(
            centrifugo_token=self.req.auth_data.get("websocket_token"),
            centrifugo_url=self.req.auth_data.get("websocket_url"),
            api_token=self.req.auth_data.get("api_token")
        )
        """

    def get_basic_html(self, user_agent: str, cookie: str):
        response = self.scraper.get(requester.basic_url, headers=get_headers(user_agent=user_agent, cookie=cookie))
        return response.text if response.status_code == 200 else CheckException(response)



    def get_artillery_info(self):
       result = self.req.request("GET", "data/getArtillery")
       return result
    

    def get_states_history(self):
        result = self.req.request("GET", "data/getStatesHistory")
        return result


    def get_history(self):
        result = self.req.request("GET", "data/getHistory")
        return result


    def get_last_action_index(self):
        result = self.req.request("GET", "data/getLastActionIndex")
        return result


    def get_alerts(self):
        result = self.req.request("GET", "data/getAlerts")
        return result



    def get_ranged_alerts(self, start_date: str, end_date: str, regionId: int):
        """
        Get alerts from region

        :param start_date: start date (2024-11-04) (YYYY-MM-DD)
        :param end_date: end date (2024-11-04) (YYYY-MM-DD)
        :param regionId: region Id (get from another functions)
        :type start_date: str
        :type end_date: str
        :type regionId: int
        """
        result = self.req.request("GET", f'/v2/data/mapGetRangedAlerts?startDate={start_date.replace("-", "")}&endDate={end_date.replace("-", "")}&regionId={regionId}&apiToken={self.req.auth_data.get("api_token")}')
        return result

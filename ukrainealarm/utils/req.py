from typing import Optional, Union
from requests import Session, Response
from ujson import dumps, loads
from .headers import get_headers
from .exceptions import CheckException


class requester:
	session = Session()

	basic_url: str = "https://map.ukrainealarm.com/"
	api: str = f"{basic_url}api"
	
	def __init__(self, auth_data: dict, user_agent: str, cookie: str):
		self.auth_data = auth_data
		self.user_agent=user_agent
		self.cookie = cookie

	def request(self, method: str, endpoint: str, body: Union[bytes, str, dict] = None, content_type: Optional[str] = "application/json; charset=UTF-8", successful_code: int = 200, json: bool = True, api: str = None) -> dict | Response:
		if not endpoint.startswith("/"): endpoint = f"/{endpoint}"
		if body:
			if isinstance(body, bytes): body = loads(body.decode('utf-8'))
			elif isinstance(body, str): body = loads(body).encode("utf-8")
			elif isinstance(body, dict): body = dumps(body).encode("utf-8")
			else: raise ValueError(f"Invalid request body type: \"{body.__class__.__name__}\"")

		print(f"{self.api}{endpoint}")
		result = self.session.request(method, f"{self.api if api is None else api}{endpoint}", data=body, headers=get_headers(content_type=content_type, user_agent=self.user_agent, cookie=self.cookie, token=self.auth_data.get("api_token")))
		if result.status_code != successful_code: CheckException(result)
		return result.json() if json else result
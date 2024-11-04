from requests import Response


class UnknownError(Exception):
	def __init__(*args, **kwargs):
		Exception.__init__(*args, **kwargs)


def CheckException(response: Response):
    raise UnknownError(f"Status: {response.status_code}\nText: {response.text}")
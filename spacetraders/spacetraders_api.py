# import sys
# sys.path.append('C:/Source/PyAPI')
from pyapi.api_comm import APICommunication


class SpaceTradersConnection():
    def __init__(self, token):
        self.api = APICommunication("https://api.spacetraders.io/v2/")
        self.token = token

    def register_as_new_agent(self):
        endpoint = "register"

        headers = {
            'Content-Type': "application/json",
        }

        data = {
            "symbol": "JavaWarlord",
            "faction": "COSMIC"
        }
        response = self.api.send_post_request(
            endpoint, headers=headers, data=data)
        return response

    def get_agent(self):
        endpoint = "my/agent"
        headers = {
            'Authorization': "Bearer " + self.token
        }
        response = self.api.send_get_request(endpoint, headers=headers)

        data = response['data']
        return data

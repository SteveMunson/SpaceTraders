from api.api_comm import APICommunication


class SpaceTradersConnection():
    def __init__(self, token):
        self.api = APICommunication("https://api.spacetraders.io/v2/")
        self.token = token

    def get_agent(self):
        endpoint = "my/agent"
        headers = {
            "Authorization": "Bearer " + self.token
        }
        response = self.api.send_get_request(endpoint, headers=headers)
        if response.status_code == 200:
            data = response.json()['data']
            return data

    def register_as_new_agent(self):
        endpoint = "register"

        headers = {
            "Content-Type": "application/json",
        }

        data = {
            "symbol": "JavaWarlord",
            "faction": "COSMIC"
        }
        response = self.api.send_post_request(
            endpoint, headers=headers, data=data)
        return response

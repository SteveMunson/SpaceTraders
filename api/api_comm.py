import requests


class APICommunication:
    def __init__(self, base_url):
        self.base_url = base_url

    def send_get_request(self, endpoint, params=None, headers=None) -> requests.Response:
        url = self.base_url + endpoint
        return requests.get(
            url, params=params, headers=headers, timeout=10)

    def send_post_request(self, endpoint, data=None, headers=None):
        url = self.base_url + endpoint
        return requests.post(url, json=data, headers=headers, timeout=10)

    def send_put_request(self, endpoint, data=None, headers=None):
        url = self.base_url + endpoint
        return requests.put(url, json=data, headers=headers, timeout=10)

    def send_delete_request(self, endpoint, headers=None):
        url = self.base_url + endpoint
        return requests.delete(url, headers=headers, timeout=10)

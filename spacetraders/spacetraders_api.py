'''
This module handles communications between our client and the api.
'''

from api.api_comm import APICommunication


class SpaceTradersConnection():
    def __init__(self, token):
        self.api = APICommunication("https://api.spacetraders.io/v2/")
        self.token = token

#
# SYSTEM
#

    def list_systems(self) -> list:
        """
        Return a paginated list of all systems.
        """
        endpoint = 'systems'
        headers = {
            "Authorization": "Bearer " + self.token
        }
        data = []
        response = self.api.send_get_request(endpoint, headers=headers)
        if response.status_code == 200:
            data = response.json()['data']
        return data

    def get_system(self, system_symbol='X1-OE') -> dict:
        """
        Get the details of a system.

        Keyword arguments:
            system_symbol -- The system symbol (default X1-OE)

        """
        endpoint = f'systems/{system_symbol}'
        headers = {
            "Authorization": "Bearer " + self.token
        }
        data = {}
        response = self.api.send_get_request(endpoint, headers=headers)
        if response.status_code == 200:
            data = response.json()['data']
        return data

    def list_waypoints_in_system(self, system_symbol='X1-OE') -> list:
        """
        Return a paginated list of all of the waypoints for a given system. 
        If a waypoint is uncharted, it will return the Uncharted trait instead of its actual traits.

        Keyword arguments:
            system_symbol -- The system symbol (default X1-OE)

        """
        endpoint = f'systems/{system_symbol}/waypoints'
        headers = {
            "Authorization": "Bearer " + self.token
        }
        data = {}
        response = self.api.send_get_request(endpoint, headers=headers)
        if response.status_code == 200:
            data = response.json()['data']
        return data

    def get_waypoint(self, waypoint_symbol: str) -> dict:
        """
        View the details of a waypoint.
        If the waypoint is uncharted, it will return the 'Uncharted' trait instead of its actual traits.

        Keyword arguments:
            waypoint_symbol -- The waypoint symbol (required)

        """
        system_symbol = waypoint_symbol[:waypoint_symbol.rfind("-")]
        endpoint = f'systems/{system_symbol}/waypoints/{waypoint_symbol}'
        headers = {
            "Authorization": "Bearer " + self.token
        }
        data = {}
        response = self.api.send_get_request(endpoint, headers=headers)
        if response.status_code == 200:
            data = response.json()['data']
        return data
#
#
#

    def get_contracts(self):
        endpoint = "my/contracts"
        headers = {
            "Authorization": "Bearer " + self.token
        }
        response = self.api.send_get_request(endpoint, headers=headers)
        if response.status_code == 200:
            data = response.json()['data']
            return data

    def get_system_symbol(self, waypoint_symbol):
        symbols = waypoint_symbol.split("-")
        return symbols[0]+"-"+symbols[1]

#
# AGENT
#
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

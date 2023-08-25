from spacetraders import credentials
from spacetraders.agent import Agent
from spacetraders.spacetraders_api import SpaceTradersConnection
from spacetraders.waypoint import Waypoint

token = credentials.token
connection = SpaceTradersConnection(token)

agent = Agent(connection.get_agent())
print(agent)

systems = connection.list_systems()
print(f"Systems: {len(systems)}")
for system in systems:
    print(system['symbol'])

print(connection.get_system(systems[0]['symbol']))
for waypoint in connection.list_waypoints_in_system(system_symbol=systems[0]['symbol']):
    print(f"WP: {waypoint['symbol']}")

print(connection.get_waypoint(waypoint['symbol']))

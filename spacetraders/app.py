import credentials
from spacetraders.agent import Agent
from spacetraders.spacetraders_api import SpaceTradersConnection

token = credentials.token
connection = SpaceTradersConnection(token)

agent = Agent(connection.get_agent())
print(agent)

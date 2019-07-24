from gremlin_python.driver import client, serializer


def get_items(client):
    callback = client.submitAsync("g.V().order().by()")
    return callback.result()

client = client.Client(
    'ws://localhost:8901/',
    'g',
    username="/dbs/tasks/colls/items",
    password="C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw/Jw==",
    message_serializer=serializer.GraphSONSerializersV2d0()
)

print("Welcome to Azure Cosmos DB + Gremlin on Python!\n")

# Insert all vertices
input("Returning all items in graph (Press Enter to Continue)")
items = get_items(client).all()
print(items.result())

# Cosmos Emulator Gremlin Test

## Installation

1. Install the emulator as mentioned [here](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator#installation)
2. Install the Python3 dependencies using `pip install -r requirements.txt`
3. Enable the Gremlin API as mentioned [here](https://github.com/MichalWierzbinski/cosmosdb-emulator-gremlin)
	`.\CosmosDB.Emulator.exe /EnableGremlinEndpoint`
4. Create a new Container with the following details:
	- Database id: `tasks`
	- Container id: `items`
	- Partition key: `/category`
	- (the other fields can be left at their default values)
5. Create a new item in the `items` container (click on the items container, click on the `New Item` button the appears on the top)
6. Run the `main.py` script, and you should see the created item(s) printed out to stdout

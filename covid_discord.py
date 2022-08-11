from discord.ext import commands
import requests
import json

client = commands.Bot(command_prefix="%")

class Data:
    def __init__(self, api_key, project_token):
        self.data = None
        self.api_key = api_key
        self.project_token = project_token
        self.params = {
            "api_key": self.api_key
        }
        self.get_data()

    def get_data(self):
        response = requests.get(f'https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}/last_ready_run/data',
                                params=self.params)
        self.data = json.loads(response.text)

    def get_total_cases(self):
        data = self.data['total']
        for content in data:
            if content['name'] == "Coronavirus Cases:":
                return content['value']

    def get_total_deaths(self):
        data = self.data['total']
        for content in data:
            if content['name'] == "Deaths:":
                return content['value']
        return ""

    def get_country_data(self, country):
        data = self.data["country"]
        if country.lower() == "america":
            countryCopy = "USA"
        elif country.lower() == "south korea":
            countryCopy = "S. Korea"
        else:
            countryCopy = country
        for content in data:
            if content['name'].lower() == countryCopy.lower():
                if content['selection3'][1:] == "":
                    return f"Cases: {content['selection1']}\nDeaths: {content['selection2']}\nCases today: N/A"
                else:
                    return f"Cases: {content['selection1']}\nDeaths: {content['selection2']}\nCases today: {content['selection3'][1:]}"
        return "Invalid data"


@client.event
async def on_ready():
    print("Covid bot is ready!")


@client.command()
async def case(ctx, *, country):
    data = Data(API_KEY, PROJECT_TOKEN)
    await ctx.send(data.get_country_data(country))


client.run(BOT_TOKEN)

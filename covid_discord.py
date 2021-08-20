
from discord.ext import commands
from selenium import webdriver


client = commands.Bot(command_prefix="%")

@client.event
async def on_ready():
    print("Covid bot is ready!")

@client.command()
async def case(ctx, *, country):
    PATH = "/Users/karan/Downloads/chromedriver"
    driver = webdriver.Chrome(PATH)
    if country.lower() == "vietnam":
        country = "viet-nam"
    elif country.lower() == "usa" or country.lower() == "america":
        country = "us"
    elif country.lower() == "uae" or country.lower() == "united arab emirates":
        country = "united-arab-emirates"
    try:
        driver.get(f"https://www.worldometers.info/coronavirus/country/{country.lower()}")
        dayCase = driver.find_element_by_class_name("news_date")
        textDay = dayCase.text.split(" ")
        cases = driver.find_element_by_class_name("news_li")
        textDisplay = cases.text.split(" ")
        await ctx.send(f"\nLatest report: {textDay[1]} {textDay[0]} has {textDisplay[0]} cases")

        driver.quit()
    except:
        await ctx.send("Please enter a valid country")
        driver.quit()





client.run('secret!')

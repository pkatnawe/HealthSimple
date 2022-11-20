from requests_html import HTMLSession
import cohere
from bs4 import BeautifulSoup
import requests
api_key = 'y1eSPIg8WROzQCQh1Vmj7vBtSkHcKYXQJKMKAaLU'
co = cohere.Client(api_key)
session = HTMLSession()
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0'
}
# def web_scraper(string):
#     url = 'http://www.webmd.com/diet/health-benefits-' + string
#     response = requests.get(url, headers=headers)
#     print(response.content)
#     soup = BeautifulSoup(response.content, 'html.parser')
#     elements = soup.find(class_= "article-page active-page")
#     test = elements.text
#     prompt = f"""Passage: Is Wordle getting tougher to solve? Players seem to be convinced that the game has gotten harder in recent weeks ever since The New York Times bought it from developer Josh Wardle in late January. The Times has come forward and shared that this likely isn't the case. That said, the NYT did mess with the back end code a bit, removing some offensive and sexual language, as well as some obscure words There is a viral thread claiming that a confirmation bias was at play. One Twitter user went so far as to claim the game has gone to "the dusty section of the dictionary" to find its latest words.

#     TLDR: Wordle has not gotten more difficult to solve.
#     --
#     Passage: ArtificialIvan, a seven-year-old, London-based payment and expense management software company, has raised $190 million in Series C funding led by ARG Global, with participation from D9 Capital Group and Boulder Capital. Earlier backers also joined the round, including Hilton Group, Roxanne Capital, Paved Roads Ventures, Brook Partners, and Plato Capital.

#     TLDR: ArtificialIvan has raised $190 million in Series C funding.
#     --
#     Passage: {test}
#     TLDR:"""
#     response = co.generate(
#     model='xlarge',
#     prompt = prompt,
#     max_tokens=250,
#     temperature=0.8,
#     stop_sequences=["--"])
#     summary = response.generations[0].text
#     return summary


def web_scraper(string):
    summaries = []
    for word in string:
        url = 'http://www.webmd.com/diet/health-benefits-' + word
        response = requests.get(url, headers=headers)
        print(response.content)
        soup = BeautifulSoup(response.content, 'html.parser')
        elements = soup.find(class_="article-page active-page")
        test = elements.text
        prompt = f"""

    Brown Rice Description: Rice has been a staple of the human diet for thousands of years. Some rice farming tools from China date back 8,000 years, and some remains of ancient rice are up to 2,000 years older than that. Brown rice means you’re eating the rice as a whole grain. That’s important because the less processed the grain, the more nutrients you get. The bran and germ, the two outer layers of brown rice, contain most of the vitamins and minerals in the grain. Those layers get removed when manufacturers make white rice, and that’s why brown rice is the healthier choice.Brown rice has a low glycemic index (GI), meaning it doesn’t cause your blood sugar to spike after you eat. Studies show that by eating three servings per day of whole grains like brown rice, you can reduce your risk of developing type 2 diabetes by up to 32%. White rice, on the other hand, can increase your risk of diabetes. Another study found that people who eat a lot of white rice are about 17% more likely to develop diabetes than folks who eat less. Scientists estimate that by replacing about 50 grams per day of white rice with brown rice, a person can reduce their diabetes risk by 16%. Many of the nutrients in brown rice help keep your heart healthy. It’s a rich source of dietary fiber, which can reduce your risk of death from heart disease. Brown rice also contains high levels of magnesium, which can help make you less vulnerable to heart disease and stroke. Overall, studies show that eating more whole grains, including brown rice, could reduce your risk of heart disease by up to 22% and your risk of stroke by as much as 12%.\n\nTLDR: Brown rice means you are eating the rice as a whole grain. This is important because the less processed the grain the more nutrients you get. Brown rice has a low glycemic index (GI) which means it won\'t spike your blood sugar and reduce the risk of developing type 2 diabetes. In addition, studies show that brown rice may reduce your risk of heart disease by up to 22%. The heart health benefits may be attributed to the high levels of dietary fibre and magnesium.  \n\n--\n\nPassage:{test} \n\n\nTLDR:'
    """
        response = co.generate(
            model='2f0307ac-4d45-472d-9d30-8b1d84baac46-ft',
            prompt=prompt,
            max_tokens=200,
            temperature=0.8,
            k=0,
            p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop_sequences=["--"],
            return_likelihoods='NONE')
        text = response.generations[0].text
        summaries.append(text)
    return summaries

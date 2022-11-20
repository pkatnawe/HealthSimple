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

Passage:{test} \n\n\nTLDR:'
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

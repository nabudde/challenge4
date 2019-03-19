import click
import requests


API_KEY = "2c6d0b1d57474731a49a989af03a13b9"

@click.command()
def main():
    """ CEND is news api that gives the user the following;
User is offered a list of four news sources.
User should be able to make a choice of a preferred news source.
User gets back a list of the top 10 headlines from the preferred source.
user is able to get news headline like a title, description and a url if they want to follow the story.
"""
    pass

def name_of_newssource():
    """ Lists of 4 newssources from the API  """

     url =  "https://newsapi.org/v2/top-headlines?sources=google-news-br&apiKey=2c6d0b1d57474731a49a989af03a13b9"
    #fetch data in json
    open_source = requests.get(url).json
    #get all articles in a string src
    src = open_source["src"]
    #empty list which will contain latest news srcs
    news_sources = []
    for s in src:
        news_sources.append(s["id"])
        for i in range (4):
            click.echo(news_sources[i])
@click.command()
def topheadlines():
    newss = click.prompt("please enter the listsource you want")
    #my_url = ("https://www.newsbtc.com/2019/03/13/crypto-market-at-major-crossroads-litecoin-ltc-bch-trx-ada-price-analysis&apiKey=2c6d0b1d57474731a49a989af03a13b9+sources=newss")this has an error
    my_url = ("https://newsapi.org/v2/top-headlines?country= "",&apiKey=071e45425325426b95797acf24ccb292
    
    #fetch dat from json
    open_headline = requests.get(my_url).json()
    #get all headlines in a string articles
    headline = open_headline["articles"]#we use articles bcz we want to be able acess the headlines
    #print("############# article 1: ",headline
    for j in headline:
        click.echo('\n')
        click.echo(click.style('TITLE:' + j['title'],fg='red'))#fg stands for foreground
        if j['description']:#we are looking for we want to know if in our list  one of them is descriped it should be printed
    #and the ones that are not descriped they should be ignored and print the described
             print(j['description'])
            # if description is nontype or null or empty -> skip
        click.echo(click.style('DOMAIN:' + j['url'], fg='green'))#we want the use to be able to follow the headlines by folowing this url

topheadlines()#we call the function

if __name__ == '__main__':
    main()
    # print("#########################  we are running the application ")

    


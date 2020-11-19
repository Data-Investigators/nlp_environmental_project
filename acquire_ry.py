# Imports

import pandas as pd
import numpy as np
from requests import get
from bs4 import BeautifulSoup
import os
# scroll down for exercise functions

###### project functions #########
def make_soup(url):
    '''
    This helper function takes in a url and requests and parses HTML
    returning a soup object.
    '''
    # set headers and response variables
    headers = {'User-Agent': 'Codeup Data Science'} 
    response = get(url, headers=headers)
    # use BeartifulSoup to make object
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


def github_urls():
    '''
    This function scrapes all of the evironmental urls from
    the github search page and returns a list of urls.
    '''
    # The base url for the main Codeup blog page
    url = 'https://github.com/search?o=desc&p=1&q=environmental&s=&type=Repositories'
    
    # Make request and soup object using helper
    soup = make_soup(url)
    
    # Create a list of the anchor elements that hold the urls.
    urls_list = soup.find_all('a', class_='v-align-middle')
    # for each url in the find all list get just the 'href' link
    urls = {link.get('href') for link in urls_list}
    # make a list of these urls
    urls = list(urls)
    return urls
# this gets 1st 10 urls, will need to get next 10 pages


def get_github(cached=False):
    '''
    This function with default cached == False does a fresh scrape of github pages returned from
    search of 'environmental' and writes the returned df to a json file.
    cached == True returns a df read in from a json file.
    '''
    # option to read in a json file instead of scrape for df
    if cached == True:
        df = pd.read_json('readmes.json')
        
    # cached == False completes a fresh scrape for df    
    else:
        # get url list
        url_list = github_urls()

        # Set base_url that will be used in get request
        base_url = 'https://github.com'
        
        # List of full url needed to get readme info
        readme_url_list = []
        for url in url_list:
            full_url = base_url + url
            readme_url_list.append(full_url)
        
        # Create an empty list, readmes, to hold our dictionaries
        readmes = []

        for readme_url in readme_url_list:
            # Make request and soup object using helper
            soup = make_soup(readme_url)

            if soup.find('article', class_="markdown-body entry-content container-lg") != None:            
                # Save the text in each readme to variable text
                content = soup.find('article', class_="markdown-body entry-content container-lg").text
            
            if soup.find('span', class_="text-gray-dark text-bold mr-1") != None:
            # Save the first language in each readme to variable text
                # NOTE: this is the majority language, not all of the languages used
                language = soup.find('span', class_="text-gray-dark text-bold mr-1").text

                # anything else useful on the page?

                # Create a dictionary holding the title and content for each blog
                readme = {'language': language, 'content': content}

                # Add each dictionary to the articles list of dictionaries
                readmes.append(readme)
            
        # convert our list of dictionaries to a df
        df = pd.DataFrame(readmes)

        # Write df to a json file for faster access
        df.to_json('readmes.json')

    
    return df





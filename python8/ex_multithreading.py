''' Multithreading Example 
Real world ex - Multithreading for I/O bound tasks
Scenario: Web Scraping
Web scraping is a common task that involves making multiple HTTP requests to fetch data from different web pages.
Since these requests are I/O bound (waiting for responses from the server), multithreading can significantly speed
up the process by allowing multiple requests to be made concurrently.
In this example, we will use the `requests` library to fetch data from multiple URLs concurrently'''

'''
URLs we will be using for web scraping

https://python.langchain.com/v0.2/docs/introduction/
https://python.langchain.com/v0.2/docs/concepts/
https://python.langchain.com/v0.2/docs/tutorials/

'''

# we will be using bs4 library for web scraping

import threading
import requests
from bs4 import BeautifulSoup

urls = [
    "https://python.langchain.com/v0.2/docs/introduction/",
    "https://python.langchain.com/v0.2/docs/concepts/",
    "https://python.langchain.com/v0.2/docs/tutorials/",
    "https://rakuten.udemy.com/course/",
    "https://google.com/"
]

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f"Fetched {len(soup.text)} characters from {url}") #here we are printing how many characters are there in URL

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All web pages fetched")    






     #html.parser is a built-in parser in Python's standard library that can parse HTML and XML documents.
    #It is used to create a parse tree from the HTML content, allowing us to navigate and extract data from the HTML structure.
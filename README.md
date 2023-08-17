# Python web projects
PROJECT NAME: 
Web Scraping and Data Extraction from Yahoo! Finance for Market Analysis

OBJECTIVE
Scraped Yahoo! Finance website https://finance.yahoo.com/  to obtain market data related to  Symbols,  Names, Prices, Change, % Change, Volume, Avg_vol(last 3 months), Market Cap and PE ratio of the 25 most active stocks.

TECHNOLOGIES 

Python 3.11.3

Python Modules

* BeautifulSoup4
    * Allows a web page to be scraped (parses its HTML or XML)
* requests
    * Allows sending HTTP requests
* pandas — Allows the data to be aligned in a tabular fashion in rows and columns


CHALLENGES:
Parsing Complex HTML Structure: The structure of Yahoo! Finance's website required understanding and navigating through complex HTML tags for data extraction.

Resolution: To tackle this challenge, I invested time in learning HTML and CSS, the fundamental languages that websites are built upon. By understanding HTML and CSS, I was able to navigate through the complex website structure and successfully gather the market data for the most active stocks. This experience not only improved my web scraping skills but also expanded my understanding of web technologies.


RESULTS:
 
- Successfully scraped market data for the 25 most active stocks from Yahoo! Finance website.

- Obtained key financial information, including Prices, Change, % Change, Volume, Avg_vol (last 3 months), Market Cap, and PE ratio.



PROJECT NAME:  
Scraping and Compiling Book Catalog Data for Analysis

OBJECTIVE
Scraped 10 webpages of a book catalogue website, http://books.toscrape.com to obtain data related to titles, prices and star-ratings of 200 books.


TECHNOLOGIES
— Python 3.11.3
— Python Modules

* BeautifulSoup4
    * Allows a web page to be scraped (parses its HTML or XML)
* requests
    * Allows sending HTTP requests
* pandas — Allows the data to be aligned in a tabular fashion in rows and columns


CHALLENGES:

Pagination and Scrolling: Scraping multiple pages of the book catalogue website required dealing with pagination and scrolling through different pages to gather all the data.

 Resolution: To address this challenge, I developed a Python solution. I created a script that dynamically generated the URLs of all ten pages and stored them in a list. Then, I implemented a function that systematically extracted each URL from the list. This function sent HTTP requests to the URLs one by one, allowing me to access the contents of each webpage programmatically. This experience emphasised the power of automation and its application in efficiently handling large amounts of data across webpages.


RESULTS:

- Gathered data from 200 books across 10 webpages of the book catalogue website.
  
- Extracted book titles, prices, and star ratings for comprehensive data collection.



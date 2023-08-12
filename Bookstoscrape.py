import requests
from bs4 import BeautifulSoup
import pandas as pd

 

# Function to generate list of URLs for each page based on a range of page numbers
def give_url(url):
  empty_url = []
  for i in url:
     list_url = f"https://books.toscrape.com/catalogue/page-{i}.html"
     empty_url.append(list_url)  
  return empty_url


# Function to scrape book data from a list of URLs
def scrape_page(urls):
   book_list = []
   for each_url in urls:
     response = requests.get(each_url)
     if response.status_code == 200:
        print("Request successful!")
        page_content = response.text      
        soup = BeautifulSoup(page_content, 'html.parser')
        ol_tag = soup.find('ol')   
        article_tag = ol_tag.find_all('article', class_= 'product_pod')
        for article in article_tag:
               h_tag = article.find('a', attrs={'title' : True})
               bookname = h_tag.attrs['title']
               p_tag = article.find('p')
               star_rate = p_tag.attrs['class'][1]
               p_tag2 = article.find('p', class_= 'price_color')
               price = p_tag2.text
               price = price[2:]  # Removing the currency symbol
               book_list.append([bookname, price, star_rate])

     else:
        print("Request failed with status code:", response.status_code)

   return book_list

# Create a range of page numbers (1 to 10)
my_url = range(1, 11)

# Generate URLs using the give_url function
saved_url = give_url(my_url)

# Scrape book data using the scrape_page function
books_lists = scrape_page(saved_url)

# Print the scraped book data
print(books_lists)


df = pd.DataFrame(books_lists, columns = ['Title', 'Price', 'Star_rating'])
# Reset the index and drop the current index column
df.reset_index(drop=True, inplace=True)
# Add 1 to each index value to start from 1 instead of 0
df.index += 1
df.to_csv('final_listof_bookstoscrape_2.csv', index=True)     







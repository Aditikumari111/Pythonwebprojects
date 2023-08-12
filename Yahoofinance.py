import requests
from bs4 import BeautifulSoup
import pandas as pd


#get the URL using response variable
my_url = "https://finance.yahoo.com/most-active"
response = requests.get(my_url)   

#Catching Exceptions
if response.status_code == 200:
    print("Request successful!")
    print("Response Content:")
    print(response.text[:500])
else:
    print("Request failed with status code:", response.status_code)

# Create a function to retrieve HTML data of the webpage as a Beautiful Soup object.
def get_page(url):
  page_content = response.text
  soup1 = BeautifulSoup(page_content, 'html.parser')
  return soup1

soup = get_page(my_url)



# Function to extract text from a list of tags and display them with an index
def tag_taker(tags):
    len_taker = len(tags)
    parameter_list = []
    for i in range(1, len_taker + 1):   
          parameter_heading = tags[i-1].text     
          parameter_list.append(parameter_heading)  
          print(str(i)+ ") " + parameter_heading)
    return parameter_list



# Function to extract text from two tags and display them
def tag_taker2(tag):
    span_list = []
    for span in tag:
        spanfind = span.find('span')
        spantext = spanfind.text
        span_list.append(spantext)
        print(spantext)
    return span_list


print("\nSYMBOLS\n")
a_tags = soup.find_all('a', attrs={'data-test': 'quoteLink'})
symbols_data =  tag_taker(a_tags) 

print('\n\n')

print("PRICES\n") 
td1_tags = soup.find_all('td', attrs= {'aria-label': "Price (Intraday)"})
prices_data = tag_taker(td1_tags)

print('\n\n')

print("\nCHANGE\n")
finstreamer3_tags = soup.find_all('fin-streamer', attrs= {'class' :"Fw(600)", 'data-field':"regularMarketChange"}) #it'll form a list
give_change = tag_taker2(finstreamer3_tags)


print('\n\n')

print("\nPERCENT CHANGE\n")
finstreamer4_tags = soup.find_all('fin-streamer', attrs= {'class' :"Fw(600)", 'data-field':"regularMarketChangePercent"}) #it'll form a list
give_percentchange = tag_taker2(finstreamer4_tags)


print('\n\n')

print("NAMES\n")   
td_tags = soup.find_all('td', class_='Va(m) Ta(start) Px(10px) Fz(s)')
names_data = tag_taker(td_tags)

print('\n\n')


print("VOLUME\n")
finstreamer2_tags = soup.find_all('fin-streamer', attrs= {'data-field': "regularMarketVolume"})
volume_data = tag_taker(finstreamer2_tags)

print('\n\n')

print("AVERAGE VOLUME\n")
td3_tags = soup.find_all('td', attrs= {'aria-label' : "Avg Vol (3 month)"})
Avg_vol_data = tag_taker(td3_tags)

print('\n\n')

print("MARKET CAP\n")
finstreamer3_tags = soup.find_all('fin-streamer', attrs= {'data-field': "marketCap"})
market_cap_data = tag_taker(finstreamer3_tags)

print('\n\n')

print("PE RATIO\n")
td2_tags = soup.find_all('td', attrs= {'aria-label' : "PE Ratio (TTM)"})
PE_ratio_data = tag_taker(td2_tags)


# Convert the data to DataFrames

symbols_df = pd.DataFrame({'Symbols': symbols_data})
names_df = pd.DataFrame({'Names': names_data})
prices_df = pd.DataFrame({'Prices': prices_data})
change_df = pd.DataFrame({'Change': give_change})
percentage_change_df = pd.DataFrame({'% Change': give_percentchange})
volume_df = pd.DataFrame({'Volume' : volume_data})
Avg_vol_df = pd.DataFrame({'Avg_vol(last 3 months)': Avg_vol_data})
market_cap_df = pd.DataFrame({'Market Cap' : market_cap_data})
PE_ratio_df = pd.DataFrame({'PE ratio' : PE_ratio_data})

# Combine all the DataFrames into a single DataFrame
combined_data = pd.concat([symbols_df, names_df, prices_df, change_df, percentage_change_df, volume_df, Avg_vol_df, market_cap_df, PE_ratio_df], axis=1)


# Reset the index and drop the current index column
combined_data.reset_index(drop=True, inplace=True)

# Add 1 to each index value to start from 1 instead of 0
combined_data.index += 1

# Save the DataFrame to CSV file with the modified index
combined_data.to_csv('  New_ActiveStocks_in_market_data.csv', index=True)


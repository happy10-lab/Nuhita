#libraries used 
import yfinance as yf
import pandas as pd
import matplotlib as plt
from bs4 import BeautifulSoup

#use yfinance to extract StockData
import yfinance as yf
tesla = yf.Ticker("TSLA")
print(tesla.info)

#using history and dataframe tesla_data.set perios parameter to max
tesla_data=tesla.history(period="max")
print(tesla_data.head())

#reset the index using reset_index (inplace=True)
#display first 3 rows of tesla_data using head
tesla_data.reset_index(inplace=True)
print(tesla_data.head())

#using webscrapping to extract TESLA REVENUE DATA
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import yfinance as yf 

def make_graph(stock_data, revenue_data, stock_name):
    
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                        subplot_titles=(f'{stock_name} Stock Price', f'{stock_name} Revenue'),
                        vertical_spacing=0.1,
                        specs=[[{"secondary_y": True}], [{"secondary_y": True}]])

    
    fig.add_trace(go.Scatter(x=stock_data['Date'], y=stock_data['Close'].astype(float),
                             name='Stock Price'), row=1, col=1, secondary_y=False)

    
    fig.add_trace(go.Bar(x=revenue_data['Date'], y=revenue_data['Revenue'].astype(float),
                         name='Revenue'), row=1, col=1, secondary_y=True)

    
    fig.update_yaxes(title_text='Stock Price ($)', row=1, col=1, secondary_y=False)
    fig.update_yaxes(title_text='Revenue ($ Millions)', row=1, col=1, secondary_y=True)   
    fig.add_trace(go.Scatter(x=stock_data['Date'], y=stock_data['Close'].astype(float),
                             name='Stock Price'), row=2, col=1, secondary_y=False)
  
    fig.add_trace(go.Bar(x=revenue_data['Date'], y=revenue_data['Revenue'].astype(float),
                         name='Revenue'), row=2, col=1, secondary_y=True)
 
    fig.update_yaxes(title_text='Stock Price ($)', row=2, col=1, secondary_y=False)
    fig.update_yaxes(title_text='Revenue ($ Millions)', row=2, col=1, secondary_y=True)

    fig.update_layout(title_text=f'{stock_name} Stock Price and Revenue',
                      xaxis_rangeslider_visible=True, 
                      height=800) 
   
    fig.show()

tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="max")

tesla_data.reset_index(inplace=True)

tesla_data['Date'] = pd.to_datetime(tesla_data['Date'])


tesla_data = tesla_data[tesla_data['Date'] <= '2021-06-30']

print("Tesla Stock Data (first 5 rows):")
print(tesla_data.head())
print("\nTesla Stock Data (info):")
print(tesla_data.info())


tesla_revenue['Date'] = pd.to_datetime(tesla_revenue['Date'])

tesla_revenue = tesla_revenue[tesla_revenue['Date'] <= '2021-06-30']

print("\nTesla Revenue Data (first 5 rows, filtered):")
print(tesla_revenue.head())
print("\nTesla Revenue Data (info, filtered):")
print(tesla_revenue.info())


make_graph(tesla_data, tesla_revenue, 'Tesla')
            # Ensure there are at least 2 columns (Date and Revenue)
            if len(cols) >= 2:
                date = cols[0].text.strip()
                revenue = cols[1].text.strip()

                # Remove commas and dollar signs from revenue
                revenue = revenue.replace(',', '').replace('$', '')

                # Append to DataFrame
                tesla_revenue = pd.concat([tesla_revenue, pd.DataFrame([{"Date": date, "Revenue": revenue}])], ignore_index=True)
        break
print(tesla_revenue.head())

tesla_revenue["Revenue"] = pd.to_numeric(tesla_revenue["Revenue"], errors='coerce')


tesla_revenue.dropna(inplace=True)

print("\nTesla Revenue DataFrame after cleaning and type conversion:")
print(tesla_revenue.head())
print(tesla_revenue.info())


#Extract GME Revenue Data
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import yfinance as yf
def make_graph(stock_data, revenue_data, stock_name):
   
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                        subplot_titles=(f'{stock_name} Stock Price', f'{stock_name} Revenue'),
                        vertical_spacing=0.1,
                        specs=[[{"secondary_y": True}], [{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=stock_data['Date'], y=stock_data['Close'].astype(float),
                             name='Stock Price'), row=1, col=1, secondary_y=False)
    fig.add_trace(go.Bar(x=revenue_data['Date'], y=revenue_data['Revenue'].astype(float),
                         name='Revenue'), row=1, col=1, secondary_y=True)
    fig.update_yaxes(title_text='Stock Price ($)', row=1, col=1, secondary_y=False)
    fig.update_yaxes(title_text='Revenue ($ Millions)', row=1, col=1, secondary_y=True)
    fig.add_trace(go.Scatter(x=stock_data['Date'], y=stock_data['Close'].astype(float),
                             name='Stock Price'), row=2, col=1, secondary_y=False)
    fig.add_trace(go.Bar(x=revenue_data['Date'], y=revenue_data['Revenue'].astype(float),
                         name='Revenue'), row=2, col=1, secondary_y=True)
    fig.update_yaxes(title_text='Stock Price ($)', row=2, col=1, secondary_y=False)
    fig.update_yaxes(title_text='Revenue ($ Millions)', row=2, col=1, secondary_y=True)
    fig.update_layout(title_text=f'{stock_name} Stock Price and Revenue',
                      xaxis_rangeslider_visible=True, # Add a range slider for easier navigation
                   height=800) # Set the height of the plot
    # Display the figure
    fig.show()
gme = yf.Ticker("GME")
gme_data = gme.history(period="max")
gme_data.reset_index(inplace=True)
gme_data['Date'] = pd.to_datetime(gme_data['Date'])
gme_data = gme_data[gme_data['Date'] <= '2021-06-30']
print("GameStop Stock Data (first 5 rows):")
print(gme_data.head())
print("\nGameStop Stock Data (info):")
print(gme_data.info())
# Prepare gme_revenue (GameStop Revenue Data)
URL_gme_revenue ="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
html_data_gme_revenue = requests.get(URL_gme_revenue).text
soup_gme_revenue = BeautifulSoup(html_data_gme_revenue,"html.parser")

table_gme_revenue = soup_gme_revenue.find_all("tbody")[1]
gme_revenue_data_list = []
for row in table_gme_revenue.find_all("tr"):
    cols = row.find_all("td")
    if len(cols) >= 2: # Ensure there are enough columns
        date = cols[0].text.strip()
        revenue = cols[1].text.strip()
        # Clean revenue data: remove commas and dollar signs
        revenue = revenue.replace(',', '').replace('$', '')
        gme_revenue_data_list.append([date, revenue])
gme_revenue = pd.DataFrame(gme_revenue_data_list, columns=["Date", "Revenue"])
gme_revenue["Revenue"] = pd.to_numeric(gme_revenue["Revenue"], errors='coerce')
gme_revenue.dropna(inplace=True)
gme_revenue['Date'] = pd.to_datetime(gme_revenue['Date'])
gme_revenue = gme_revenue[gme_revenue['Date'] <= '2021-06-30']
print("\nGameStop Revenue Data (first 5 rows, filtered):")
print(gme_revenue.head())
print("\nGameStop Revenue Data (info, filtered):")
print(gme_revenue.info())
# Call the make_graph function for GameStop
make_graph(gme_data, gme_revenue, 'GameStop')

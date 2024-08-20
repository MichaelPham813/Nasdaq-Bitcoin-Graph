import nasdaqdatalink as ndl
import pandas as pd
from datetime import datetime
import plotly.express as px
import plotly.io as pio

#This function is for getting the data and cleaning the data too
#The most difficult part is converting it into date time and grab the date only instead of timestamp
#The rest is easy


#Set pandas dataframe option
pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 12)
pd.set_option('display.width', 400)

#Get API key
ndl.ApiConfig.api_key = 'JEdVxy7BgEYA_Fs5kGyn'

#Data table for Trade volume and transaction volume ratio
bitcoin_data = ndl.get_table('QDL/BCHAIN', code = 'TVTVR',paginate = True)



def trade_volume_func(number_of_row = 20):
    global bitcoin_data
    #Convert date into date time and sort the value
    bitcoin_data['date'] = pd.to_datetime(bitcoin_data['date'])
    bitcoin_data = bitcoin_data.sort_values(by = 'date')
    
    #Get bottom of data to get interesting data
    top_data_sets = bitcoin_data.tail(number_of_row)
    
    #Graph the data
    fig_1 = px.line(top_data_sets, x = 'date', y = "value")
    img_convert = pio.to_image(fig_1,'png')
    
    #Write data into file
    with open('static/images/plot_1.png',"wb") as img_file:
        img_file.write(img_convert)   
        
#Data table for Bitcoin Miner Revenue
bitcoin_miner = ndl.get_table('QDL/BCHAIN', code = 'MIREV',paginate = True)

def bitcoin_miner_func(number_of_row = 20):
    global bitcoin_miner
    #Convert date into date time and sort the value
    bitcoin_miner['date'] = pd.to_datetime(bitcoin_miner['date'])
    bitcoin_miner = bitcoin_miner.sort_values(by = 'date')
    
    #Get bottom of data to get interesting data
    top_data_sets_2 = bitcoin_miner.tail(number_of_row)
    
    #Graph the data
    fig_2 = px.bar(top_data_sets_2, x = 'date', y = "value")
    img_convert = pio.to_image(fig_2,'png')
    
    #Write data into file
    with open('static/images/plot_2.png',"wb") as img_file:
        img_file.write(img_convert)       
        

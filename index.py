from flask import Flask,render_template,request
from nasdaq_api import bitcoin_miner_func, trade_volume_func
from currency_exchange import btc_exchange

app = Flask(__name__)

cad_data,usd_data = btc_exchange()
#Creating graph and control how much data you want to graph max is 999
# trade_volume_func(50)
# bitcoin_miner_func(20)

#Default/page
@app.route('/', methods = ['GET','POST'])
def index():
  user_input = None
  if request.method == "POST":
    user_input = request.form['user_input']
    user_input = int(user_input)
    trade_volume_func(user_input)
    bitcoin_miner_func(user_input)
  return render_template("index.html",usd_data = usd_data,cad_data = cad_data)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
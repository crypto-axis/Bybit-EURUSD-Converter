from pandas_datareader import data as web
from datetime import datetime,timedelta
import pandas as pd

data = pd.read_csv('data.csv')

start = datetime(2022,5,3,1,2)
end = datetime.now()

eurdata = web.DataReader("EURUSD=X",'yahoo', start, end)
eurdata = pd.DataFrame(eurdata).reindex(index=None)
eurdata.reset_index(inplace=True)
eurdata['Date'] = pd.to_datetime(eurdata['Date'])
eurdata['Date'] = eurdata['Date']
eurdata['eurusd_price_date'] = eurdata['Date']

data['time'] = pd.to_datetime(data['time'])
data = data.to_dict('records')
eurdata = eurdata.to_dict('records')

new_eurdata = []

for i in eurdata:
    i['eurusd_price_date'] = i['eurusd_price_date'].to_pydatetime().date()
    if -1 < i['eurusd_price_date'].weekday() < 3 or  i['eurusd_price_date'].weekday() == 6:
        new_eurdata.append(i)
    else:
        new_eurdata.append(i)
        d = i.copy()
        day = d['eurusd_price_date']
        delta = timedelta(days = 1)
        day = day +delta
        d['eurusd_price_date'] = day
        new_eurdata.append(d)
        d = i.copy()
        delta = timedelta(days = 1)
        day = day +delta
        d['eurusd_price_date'] = day
        new_eurdata.append(d)

eurdata = new_eurdata

for i in data:
    op_date = i['time'].to_pydatetime().date()
    for j in eurdata:
        if j['eurusd_price_date'] == op_date:
            print(op_date ," : " ,j['eurusd_price_date'])
            i['EURUSD'] = j['Close']
            break

new_data = pd.DataFrame(data)

new_data.to_csv("new_data.csv", index=None)


from matplotlib import pyplot as plt
from pandas.io.data import DataReader
from datetime import datetime
import pandas as pd

pd.options.display.mpl_style = 'default'

# use recent 1 year as range for stock quote
end = datetime.now()
start = datetime(end.year-1, end.month, end.day)

# Read stock data from google finance
stock_label1 = 'GOOG'
stock_label2 = 'IBM'
comp1 = DataReader(stock_label1, 'google', start, end)
comp2 = DataReader(stock_label2, 'google', start, end)

# As two stocks might have different price scope,
# use relative ratio instead of absolute price for y-axis
comp1_mean = comp1['Close'].mean()
comp2_mean = comp2['Close'].mean()
comp1['adj_close'] = comp1['Close'] / comp1_mean
comp2['adj_close'] = comp2['Close'] / comp2_mean
ax = comp1['adj_close'].plot(legend=True, label=stock_label1, figsize=(10, 4))
ax2 = comp2['adj_close'].plot(legend=True, label=stock_label2, figsize=(10, 4))

# draw a vertical line indicating an event on the comparison plot
ymin = 0
ymax = max(ax.get_ylim()[1], ax2.get_ylim()[1])
event_date = datetime(2015, 1, 9)
plt.vlines(x=event_date, ymin=ymin, ymax=ymax, label=str(event_date)[:10], color='r')

# highlight the maximum and minimum stock prices for two stocks
for df in [comp1, comp2]:
	min_val = df.Close.min()
	max_val = df.Close.max()
	min_row = df[df.Close==min_val]
	max_row = df[df.Close==max_val]
	df_minxy = (min_row.index[0], min_val/df.Close.mean())
	df_maxxy = (max_row.index[0], max_val/df.Close.mean())
	price_str = '$'+str(round(min_val, 1))
	plt.annotate(price_str,xy=df_minxy)
	price_str = '$'+str(round(max_val, 1))
	plt.annotate(price_str,xy=df_maxxy)


plt.legend(loc='best')  # show the label of vertical line at a best position
# http://stackoverflow.com/questions/4700614/how-to-put-the-legend-out-of-the-plot
plt.show()




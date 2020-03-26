

#histograms
import matplotlib.pyplot as plt
import pandas as pd
Read_csv_filename = 'realEstate_trans.csv'
Read_csv_data = pd.read_csv(Read_csv_filename)
Read_csv_data = Read_csv_data.query('beds < 5')
Read_csv_data.hist(
        column='price', 
    by='beds', 
    xlabelsize=9, 
    ylabelsize=9, 
    figsize=(10,9)
)
# save to file
plt.savefig('output/histogram.pdf')
# show the figures
plt.show()

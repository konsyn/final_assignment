import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

liquor_table = pd.read_csv("path\\liquor_final.csv", encoding='utf-8')

# #### percentage of sales per store
sales_per_store = liquor_table.groupby("store_number", as_index=False)['bottles_sold'].sum()
total_sales = sales_per_store['bottles_sold'].sum()
sales_per_store['percentage'] = ((sales_per_store['bottles_sold']/total_sales)*100).round(2)
sales_per_store.to_csv("path\\sales_per_store.csv")

# #### most popular item sold based on zipcode

popularity_per_zip = liquor_table.groupby(["zip_code", 'item_description'])['bottles_sold'].sum().reset_index()
popularity_per_zip = popularity_per_zip.sort_values(['zip_code', "bottles_sold"], ascending=False)
popularity_per_zip.to_csv("path\\popularity_per_zip.csv")

# #### Visualization
number_of_drinks = popularity_per_zip['item_description'].count()

color_labels = popularity_per_zip['item_description'].unique()
rgb_values = sns.color_palette("Set1", number_of_drinks)
color_map = dict(zip(color_labels, rgb_values))

plt.scatter(x=popularity_per_zip['zip_code'], y=popularity_per_zip['bottles_sold'],
            c=popularity_per_zip['item_description'].map(color_map))
plt.ylabel('Bottles sold')
plt.xlabel("Zip code")
plt.title("Bottles sold per Zip code")
plt.show()

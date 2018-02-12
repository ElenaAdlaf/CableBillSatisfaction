"""

2-3-18

The code answers the following questions based on consumer survey data:
Compare monthy bill amount and customer satisfaction with
their cable service.
Compare household income and customer satisfaction with
their cable service.

@author: eadlaf

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# load the excel file with the data
data = pd.read_excel('F:\Tivo\Data Science Projects/2017Q4/analysis/Q2A-data-Monthly Bill Satisfaction.xlsx')

# create a dataframe with only the columns of interest included
included_columns1 = ['bill', 'rating']
rating_by_bill = data[included_columns1]
included_columns2 = ['income', 'rating']
rating_by_income = data[included_columns2]

# define the categorical subgroups, also the labels for the graphs
bill_categories = ["Less than $50", "$51 - $75", "$76 - $100", "$101 - $125", "$126 - $150", "$151+"]

income_categories = ["$0 - $50,000", "$51,000 - $100,000", "$101,000 - $150,000", "$151,000 - $200,000",
 "$201,000 - $250,000", "$251,000 - $300,000", "$301,000+"]

ratings_categories = ['Unsatisfied with the service', 'Satisfied with the service', 'Very satisfied with the service']

# define a function to calculate the percentage of each rating response for each item category
def measure_rating (dframe, column, category):
    cat = dframe[column]==category
    amount = dframe[cat]
    unsatisfied_percent = amount.rating.str.count(ratings_categories[0]).sum()/len(amount)*100
    satisfied_percent = amount.rating.str.count(ratings_categories[1]).sum()/len(amount)*100
    verysatisfied_percent = amount.rating.str.count(ratings_categories[2]).sum()/len(amount)*100
    return [unsatisfied_percent, satisfied_percent, verysatisfied_percent]

# create a dictionary with the labels and values for the bill plot
bill_rating = {}
for b in range(len(bill_categories)):
    bill_rating[bill_categories[b]] = measure_rating (dframe=rating_by_bill, column='bill', category=bill_categories[b])
bill_rating_plot = pd.DataFrame.from_dict(data=bill_rating, orient='index')
bill_rating_plot

# create a dictionary with the labels and values for the income plot
income_rating = {}
for i in range(len(income_categories)):
    income_rating[income_categories[i]] = measure_rating (dframe=rating_by_income, column='income', category=income_categories[i])
income_rating_plot = pd.DataFrame.from_dict(data=income_rating, orient='index')

# create stacked bar charts of the data
ax = bill_rating_plot.plot(kind='barh', stacked=True, title ="Customer Satisfaction Based on Bill Amount", figsize=(15,10), legend=True, fontsize=14)
ax.set_ylabel("Billing Ranges", fontsize=12)
ax.set_xlabel("Percent of Customer Response", fontsize=12)
plt.legend(('Unsatisfied', 'Satisfied', 'Very Satisfied'), fontsize=12)
plt.xlim([0,119])
plt.show()

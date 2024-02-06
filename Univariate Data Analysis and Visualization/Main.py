#Import the required libraries
import pandas as pd
pd.set_option('display.max_columns',100)
import matplotlib.pyplot as plt  
import seaborn as sns
import warnings
warnings.simplefilter('ignore')

#Load the dataset
data = pd.read_csv("vehicle_data_1.csv")

#Step 1 : Shape or Dimensions of the DataFrame
print("DF Shape")


#Step 2 : Explore Data Types of the various columns
print("DF Column Types")


#Step 3 : Explore data by displaying 5 rows
print("Top 5 rows")


#Numerical Features Plots
#create df of numeric features only.
num_cols = data.select_dtypes(exclude='object')

#Set size of figure 
cols = 3
rows = 3
fig = plt.figure(figsize=(cols*5, rows*5))
plt.subplots_adjust(hspace=0.5, wspace=0.5)

#Step 4 : Plot  Histogram for all numeric features (Use sns.histplot())
#(Set title as "Histogram" .Save in file uahistogram.png)
plt.suptitle("Histogram")
for i, col in enumerate(num_cols):
    ax=fig.add_subplot(rows,cols,i+1)
    sns.histplot(x = data[col], ax = ax)
plt.savefig("uahistogram.png")
plt.clf()

#Step 5 : Plot KDE plot for all numeric features (Use sns.kdeplot())
#(Set title as "KDE Plot" .Save in file uakdeplot.png)


#Step 6 : Plot Rug Plot for all numeric features (Use sns.rugplot())
#(Set title as "Rug Plot" .Save in file uarugplot.png)


#Step 7 : Plot Box Plot for all numeric features (Use sns.boxplot())
#(Set title as "Box Plot" .Save in file uaboxplot.png)


#Step 8 : Plot Violin Plot for all numeric features (Use sns.violinplot())
#(Set title as "Violin Plot" .Save in file uaviolinplot.png)


#Step 9 : Plot Strip Plot for all numeric features (Use sns.stripplot())
#(Set title as "Strip Plot" .Save in file uastripplot.png)


#Categorical Features Plots
#create df of categoric features only.


#Create df of categorical features where the number of unique values is less than 10


#Set size of figure


#Step 10 : Plot Count Plot for all Categoric features (Use sns.countplot())
#(Set title as "Count Plot" .Save in file uacountplot.png)


#Step 11 : Plot Pie Charts for all Categoric features (Use plt.pie()) 
plt.suptitle("Pie Chart")
for i, col in enumerate(cat_cols):
	df = data[col].value_counts()
	ax = fig.add_subplot(rows, cols, i+1)
	plt.pie(df, labels=df.index, autopct="%.0f%%")
plt.savefig("uapiechart.png")
plt.clf()

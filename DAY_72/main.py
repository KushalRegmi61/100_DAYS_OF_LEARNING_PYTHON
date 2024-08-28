import pandas as pd
#setting pandas to format ouptut like 1,300.00
pd.options.display.float_format = '{:,.2f}'.format

df = pd.read_csv("salaries_by_college_major.csv")
df.head()
df.shape
df.columns
df.isna()
clean_df=df.dropna()
clean_df.tail()
clean_df['Undergraduate Major'].idxmax()
clean_df['Undergraduate Major'].loc[8]
id =clean_df['Starting Median Salary'].idxmin()
clean_df.loc[id]
clean_df['Mid-Career 90th Percentile Salary']-clean_df['Mid-Career 10th Percentile Salary']
col1=clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary'])
clean_df.insert(1, 'Diff', col1)
clean_df.head()
low_risk = clean_df.sort_values('Diff')

low_risk[['Undergraduate Major', 'Diff']].head()
low_risk.head()

highest_spread= low_risk['Undergraduate Major'][low_risk['Diff'].idxmax()]
print(highest_spread)

new_df=low_risk.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
new_df[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head()

low_risk.groupby('Group').count()

group_df= clean_df.groupby('Group')
print(group_df.all())
# low_risk.groupby('Group').mean()# Select only the numeric columns for calculating the mean
numeric_cols = clean_df.select_dtypes(include='number')

# Group by 'Group' column and calculate the mean of numeric columns
result = clean_df.groupby('Group')[numeric_cols.columns].mean()

print(result)


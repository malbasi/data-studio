# Drop the legend from rcParams.update:
Can't do it from rcParams? Do this
ax.legend_.remove() 
# Drop NAs from only specific columns:
df = df.dropna(subset=['columnName']
# Remove Axis labels in rcParams
    'axes.labelsize'      : 0,
# Make all bars in graph the same color
ax_rate = df_per.sort_values(by='rate', ascending=False).head(10).plot(kind='barh', x='pub_name', y='rate', color='#268BD2') <<<---
# Drop the dupes and fill.
......no?2
# Change histogram size
whatver.plot(kind='hist', bins=[0,.5,1,1.5,2,2.5,3])

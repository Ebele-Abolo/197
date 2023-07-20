dataframe.groupby([‘column_name’, ‘column_name’])[‘column_name’].mean().reset_index()
sns.heatmap( dataframe , cmap= ‘colormap’)
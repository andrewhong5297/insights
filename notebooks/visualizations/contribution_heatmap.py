import matplotlib.pyplot as plt
import seaborn as sns


def contribution_heatmap(
        dataframe, 
        index_col='project_name', 
        column_col='month_year', 
        value_col='total_contributors', 
        cmap='Greens', 
        vmin=0, 
        vmax=10, 
        linewidths=1,
        scaler=.2,
        figsize=None,
        sort_label_method='first',
        dpi=300):
    

    df = dataframe.pivot_table(index=index_col, columns=column_col, values=value_col)
    if sort_label_method == 'first':
        labels = dataframe.groupby(index_col)[column_col].first().sort_values().index
    if sort_label_method == 'sum':
        labels = df.sum(axis=1).sort_values(ascending=False).index
    if sort_label_method == 'mean':
        labels = df.fillna(0).mean(axis=1).sort_values(ascending=False).index        

    if figsize is None:
        figsize = (len(df.columns)*scaler, len(df)*scaler)
    fig, ax = plt.subplots(figsize=figsize, dpi=dpi, facecolor='white')

    sns.heatmap(
        df.reindex(labels), 
        cmap=cmap, 
        vmin=vmin, 
        vmax=vmax, 
        linewidths=1,
        cbar=False, 
        ax=ax
    )
    ax.xaxis.set_ticks_position('top')
    ax.tick_params(axis='x', labelrotation = 90)
    ax.set_xlabel("")
    ax.set_ylabel("")

    fig.tight_layout()

    return fig, ax
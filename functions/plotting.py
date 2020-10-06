import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objs as go
from wordcloud import WordCloud, STOPWORDS


# Objects included in this file:

# Functions included in this file:
# # plot_empty (mpl)
# # plot_heatmap (sns)
# # plot_bar (plotly)
# # plot_double_line (plotly)


def plot_empty(xlabel=None, ylabel=None,
               title=None,
               figsize=(8, 5)):
    """Initialize fig object for seaborns objects that do not include fig by default
    """
    fig = plt.figure(figsize=figsize, dpi=80)

    ax = fig.gca()
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.set_title(title, fontsize=16)

    return fig, ax


def plot_heatmap(df, xlabel=None, ylabel=None, title=None,
                 xticklabels=None, yticklabels=None,
                 color='coolwarm', annot=False, fmt=None,
                 order=None, figsize=(8, 5), dpi=240):
    """Heatmap is the same dimensions as input table
    """
    fig = plt.figure(figsize=figsize, dpi=dpi)

    if order:
        df = df[order]
    
    # annotations
    if fmt:
        sns.heatmap(df, cmap=color, annot=annot, fmt=fmt)
    else:
        sns.heatmap(df, cmap=color, annot=annot)

    ax = fig.gca()
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if xticklabels:
        ax.set_xticklabels(xticklabels)
    if yticklabels:
        ax.set_yticklabels(yticklabels)
    ax.set_title(title)
    return fig, ax


def plot_bar(df, x, y, xlabel=None, ylabel=None, title=None,
             ymin=None, ymax=None, ydtick=0.1,
             colors=None):
    """Takes a dataframe with the following format:
     x_col  | y_col  
    --------+---------
     x_val1 | y_val1
     x_val2 | y_val2
     ...    | ... 
    
    """
    if colors:
        bar = go.Bar(x=df[x],
                     y=df[y],
                     marker={'color': df[colors]}, )
    else:
        bar = go.Bar(x=df[x],
                     y=df[y], )

    fig = go.Figure()
    fig.add_trace(bar)

    fig.layout.update(xaxis={'title': xlabel,
                             'tickfont': {'size': 12}},
                      yaxis={'range': [ymin, ymax], 'dtick': ydtick,
                             'title': ylabel,
                             'tickfont': {'size': 18}, 'titlefont': {'size': 32},
                             'showgrid': True, 'gridcolor': '#E4EAF2', 'zeroline': False, },
                      title=title, titlefont={'size': 40}, title_x=0.5,
                      width=1200, height=600, autosize=False,
                      plot_bgcolor='rgba(0,0,0,0)',
                      hovermode='closest',
                      )

    return fig


def plot_double_line(df, x, y, y2,
                     xlabel=None, ylabel=None, y2label=None, title=None,
                     xrange=None, xdtick=None,
                     yrange=None, ydtick=None,
                     y2range=None, y2dtick=None):
    """Takes a dataframe with the following format:
     x_col  | y_col  | y2_col
    --------+--------+---------
     x_val1 | y_val1 | y2_val1
     x_val2 | y_val2 | y2_val2
     ...    | ...    | ...
    
    Exports a chart with two y-axes, y2 refers to the right y-axis
    """

    scatter1 = go.Scatter(x=df[x], y=df[y], name=y, line={'color': '#1f77b4'})
    scatter2 = go.Scatter(x=df[x], y=df[y2], name=y2, line={'color': '#ff7f0e'}, yaxis='y2')

    layout = go.Layout(xaxis={'range': xrange, 'dtick': xdtick,
                              'title': xlabel,
                              'titlefont': {'size': 32},
                              'tickfont': {'size': 16},
                              'showgrid': True, 'gridcolor': '#E4EAF2', 'zeroline': False,
                              },
                       yaxis={'range': yrange, 'dtick': ydtick,
                              'title': ylabel,
                              'titlefont': {'size': 32, 'color': '#1f77b4'},
                              'tickfont': {'size': 18, 'color': '#1f77b4'},
                              'showgrid': True, 'gridcolor': '#E4EAF2', 'zeroline': False,
                              },
                       yaxis2={'range': y2range, 'dtick': y2dtick,
                               'title': y2label,
                               'titlefont': {'size': 32, 'color': '#ff7f0e'},
                               'tickfont': {'size': 18, 'color': '#ff7f0e'},
                               'showgrid': True, 'gridcolor': '#E4EAF2', 'zeroline': False,
                               'side': 'right', 'overlaying': 'y',
                               },
                       title=title,
                       titlefont={'size': 40},
                       showlegend=False,
                       legend={'x': 0.75,
                               'xanchor': 'center',
                               'orientation': 'h',
                               'font': {'size': 20}},
                       width=900, height=600, autosize=False,
                       plot_bgcolor='rgba(0,0,0,0)',
                       hovermode='closest',
                       )

    fig = go.Figure(data=[scatter1, scatter2],
                    layout=layout)

    return fig


def plot_wordcloud(topics, stopwords=STOPWORDS, figsize=(10, 4)):
    """Convenience wrapper
    """
    wordcloud = WordCloud(stopwords=stopwords,
                          background_color='white',
                          width=figsize[0]*100, height=figsize[1]*100).generate(topics)
    
    fig = plt.figure(figsize=figsize)
    plt.imshow(wordcloud)
    plt.axis('off')
    
    return fig

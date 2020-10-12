import plotly.graph_objs as go


# Objects included in this file:

# Functions included in this file:
# # plot_bar
# # plot_double_line


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

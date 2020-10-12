import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS


# Objects included in this file:

# Functions included in this file:
# # plot_empty (mpl)
# # plot_heatmap (sns)
# # plot_wordcloud (mpl)


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

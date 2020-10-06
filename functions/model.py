import numpy as np
from sklearn.metrics import f1_score, auc, roc_auc_score, roc_curve, precision_score, recall_score, accuracy_score, precision_recall_curve, confusion_matrix
from sklearn.base import BaseEstimator, TransformerMixin
    
    
def compute_multiclass_ROC(y_test, y_score):
    """Takes "y_test" and "y_score" as inputs and returns the fpr, tpr, and roc_auc scores dictionary.
    From scikit-learn's plot_roc tutorial:
    https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html
    """
    
    fpr, tpr, thresholds, roc_auc = dict(), dict(), dict(), dict()
    
    # Compute micro-average ROC curve and ROC AUC
    for i in range(5):
        fpr[i], tpr[i], thresholds[i] = roc_curve(y_test[:, i], y_score[:, i])
        roc_auc[i] = roc_auc_score(y_test[:,i], y_score[:,i])

    # Collect results
    fpr["micro"], tpr["micro"], thresholds["micro"] = roc_curve(y_test.ravel(), y_score.ravel())
    roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])
    
    # Compute macro-average ROC curve and ROC area
    all_fpr = np.unique(np.concatenate([fpr[i] for i in range(5)])) # Aggregate all false positive rates

    # Interpolate all ROC curves at this points
    mean_tpr = np.zeros_like(all_fpr)
    for i in range(5):
        mean_tpr += np.interp(all_fpr, fpr[i], tpr[i])
    mean_tpr /= 5 # Average it

    # Collect Results
    fpr["macro"], tpr["macro"] = all_fpr, mean_tpr
    roc_auc["macro"] = auc(fpr["macro"], tpr["macro"])
    
    return fpr, tpr, thresholds, roc_auc


class TextSelector(BaseEstimator, TransformerMixin):
    """Used for SKLearn's pipeline
    Transformer to select a single column from the data frame to perform additional transformations on
    Use on text columns in the data
    """
    def __init__(self, key):
        self.key = key

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X[self.key]
    
    
class NumberSelector(BaseEstimator, TransformerMixin):
    """Used for SKLearn's pipeline
    Transformer to select a single column from the data frame to perform additional transformations on
    Use on numeric columns in the data
    """
    def __init__(self, key):
        self.key = key

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X[[self.key]]

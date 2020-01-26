#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import pandas as pd
import matplotlib.pyplot as plt
from mlxtend.plotting import plot_decision_regions
from matplotlib.backends.backend_pdf import PdfPages
from sklearn.model_selection import cross_val_score

def main():
    df = pd.read_csv("delay_time.csv")
    #X = df[['mean','stdev','variance','skew','kurtosis','max','rms','en']]
    #X = df[['mean','max','rms']]
    X = df[['mean','stdev']]
    Y = df['label'].map({'ECU0': 0, 'ECU1': 1, 'ECU2': 2, 'ECU3': 3, 'ECU4': 4, 'ECU5': 5, 'ECU6': 6})
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0) # dividing the data to 80% as training data, 20% as testing data
    
    # knn
    knn = KNeighborsClassifier(n_neighbors=5)
    print(np.mean(cross_val_score(knn, X, Y, cv=5)))
    knn.fit(X_train, Y_train)
    Y_pred = knn.predict(X_test)
    C = confusion_matrix(Y_test, Y_pred)
    # Normalization
    NC = C / C.astype(np.float).sum(axis=1)
    print(NC)
    for r in NC:
        for c in r:
            print("{}".format(c), end=",")
    # plot
    X_combined = np.vstack((X_train, X_test))
    y_combined = np.hstack((Y_train, Y_test))
    
    '''
    fig = plt.figure()
    plot_decision_regions(X_combined, y_combined, clf=knn)
    
    plt.xlabel('mean [ns]')
    plt.ylabel('standard deviation [ns]')
    plt.xlim(-170, 100)
    plt.ylim(0, 100)
    plt.legend(loc='upper right')
    
    pp = PdfPages('knn.pdf')
    pp.savefig(fig)

    pp.close()
    plt.close('all')
    '''

    df = pd.DataFrame(NC, index=['ECU0', 'ECU1', 'ECU2', 'ECU3', 'ECU4', 'ECU5', 'ECU6'], columns=['ECU0', 'ECU1', 'ECU2', 'ECU3', 'ECU4', 'ECU5', 'ECU6'])
    fig = plt.figure()
    sns.heatmap(df, cmap="Greens", annot=True, fmt=".4f")
    plt.yticks(rotation=0)
    
    pp = PdfPages('knn_confusion.pdf')
    pp.savefig(fig)

    pp.close()
    plt.close('all')

if __name__ == '__main__':
    main()

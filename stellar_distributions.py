# -*- coding: utf-8 -*-
"""
Yash R. Bhora
DS2001 Practicum Final Project
Distribution of Stars at Different Lightyear Thresholds based on K-means Clusters
April 8, 2022
stellar_distribution.py
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import imageio

FILENAME = "astronomy_calculations3.csv"
COLORS = ["plum", "lightcoral", "skyblue", "sandybrown", "limegreen"]
LABELS = ["Class A", "Class B", "Class C", "Class D", "Class E"]

def read_csv(filename):
    """ Function: read_csv
        Parameters: Name of CSV file to be read (string)
        Returns: dataframe with only distance and cluster color columns
    """
    df = pd.read_csv(filename)
    df = df.rename(columns={"Distance\n": "distance", "Cluster": "cluster"})
    df = df[["distance", "cluster"]]
    
    return df

def cluster_count(df, threshold):
    """ Function: cluster_count
        Paremeters: dataframe with data, list of clusters, light year threshold (float)
        Returns: list with percent distribution of each cluster
    """
    df_filt = df[df["distance"] < threshold]
    df_filt = df_filt.replace('red', 'Class D')
    df_filt = df_filt.replace('fuchsia', 'Class A')
    df_filt = df_filt.replace('orange', 'Class C')
    df_filt = df_filt.replace('green', 'Class B')
    df_filt = df_filt.replace('blue', 'Class E')
    clust_counts = df_filt["cluster"].value_counts(normalize=True).sort_index()
    
    
    return clust_counts
    
    
def main():
    df = read_csv(FILENAME)
    eighty_q = df["distance"].quantile(0.9)
    ten_q = df["distance"].quantile(0.1)
    
    # thresholds to generate plots of
    thresholds = np.linspace(round(ten_q), round(eighty_q), 20)
    
    count = 0
    filenames = []
    
    # clust_c = cluster_count(df, ten_q)
    # print(clust_c.index[0])
    
    
    for threshold in thresholds:
        filename = "hist" + str(count) + ".png"
        clust_c = cluster_count(df, threshold)
        plt.figure(dpi = 200)
        cols = clust_c.index[:len(COLORS)]
        plt.bar(cols, clust_c[:len(COLORS)], color = COLORS )
        plt.ylim(0, 1)
        plt.title("Cluster Distributions Within Radius < " + str(round(threshold)) + " ly")
        plt.xlabel("Cluster Class")
        plt.ylabel("Relative Frequency")
        plt.savefig(filename)
        plt.show()
        count += 1
        if count == 0:
            filenames += [filename] * 10
        else:
            filenames += [filename] * 3
    
    # Turn figures to GIF
    with imageio.get_writer('stellar_distributions2.gif', mode='I') as writer:
        for filename in filenames:
            image = imageio.imread(filename)
            writer.append_data(image)
    
    
main()

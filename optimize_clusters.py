# -*- coding: utf-8 -*-
"""
Yash R. Bhora
DS2001 Practicum Final Project
Optimizing K-means Clusters using Within Cluster Sum of Squares
April 8, 2022
optimize_clusters.py

"""
import numpy as np
import csv
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
import imageio
import seaborn as sns

PALETTE = sns.color_palette(None, 11)


FILENAME = "astronomy_calculations.csv"


def read_data(file):
    """ Function: read_data; reads the third and fourth column of csv where
                  lie the data of interest(color and absolute magnitude).
        Parameters: file (string); name of the file
        Returns: A list of lists containing two data points(color, abs mag)
    """
    X = []
    with open(file, "r") as csvfile:
        next(csvfile)
        data = csv.reader(csvfile)
        
        for row in data:
            tup = []
            tup.append(float(row[2]))
            tup.append(float(row[3]))
            X.append(tup)
    
    return np.array(X)

def main():
    X = read_data(FILENAME)
    
    # wcss = []
    filenames = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=len(X), n_init=10, random_state=0)
        y_kmeans = kmeans.fit_predict(X)
        plt.figure(dpi = 200)
        for j in range(i):
            plt.plot(X[y_kmeans == j, 0], X[y_kmeans == j, 1], "o", ms = 0.05, color = PALETTE[j])
            
        plt.plot(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], "o", ms = 2, c = "black", label = "Centroids")
        plt.xlabel("Color (B-V) (nm)")
        plt.ylabel("Absolute Magnitude (W/m^2) (log base 10)")
        plt.title("Color VS Absolute Magnitude, Clusters = " + str(i))
        
        filename = "Clusters_" + str(i) + ".png"
        filenames += 5 * [filename]
        plt.savefig(filename)
        plt.show()
        
    # Turn figures to GIF
    with imageio.get_writer('clusters.gif', mode='I') as writer:
        for filename in filenames:
            image = imageio.imread(filename)
            writer.append_data(image)
    """
        # wcss.append(kmeans.inertia_)
    plt.plot(range(1, 11), wcss)
    plt.title('Elbow Method')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')
    plt.show()
    
    
    plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s = 1, c = "red", label = "Cluster 1")
    plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s = 4, c = "yellow", label = "Centroids")
   
    plt.scatter(X[:,0],X[:,1], s=1, marker="o", alpha=0.5)
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=2, c='red',)
    plt.show()
    """
main()

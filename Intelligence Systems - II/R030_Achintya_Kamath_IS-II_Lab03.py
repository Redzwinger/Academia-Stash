'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Intelligence Systems - II
Lab 03
Date: 03/01/2024
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Intelligence Systems - II \n Lab 03 \n Date: 03/01/2024")

print("\n ############# ################ ####################\n")

import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn import mixture
from matplotlib.patches import Ellipse
import matplotlib.gridspec as gridspec
import warnings
warnings.filterwarnings('ignore')

# K-Means #

X, y_true = make_blobs(n_samples=1000, centers=5, cluster_std=0.69, random_state=2)

plt.scatter(X[:, 0], X[:, 1], s=50)
plt.title("Random Samples")
plt.show()

kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

plt.subplot(1,2,1)
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
plt.title("K-Means")

centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)

# GMM #

GMM = mixture.GaussianMixture
gmm = GMM(n_components=4).fit(X)
labels = gmm.predict(X)
plt.subplot(1,2,2)
plt.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap='viridis')
plt.title("Gaussian Mixture")
plt.show()

probs = gmm.predict_proba(X)
print(probs[:5].round(3))

def draw_ellipse(position, covariance, ax=None, **kwargs):
    ax = ax or plt.gca()
    
    if covariance.shape == (2, 2):
        U, s, Vt = np.linalg.svd(covariance)
        angle = np.degrees(np.arctan2(U[1, 0], U[0, 0]))
        width, height = 2 * np.sqrt(s)

    else:
        angle = 0
        width, height = 2 * np.sqrt(covariance)
    
    for nsig in range(1, 4):
        ax.add_patch(Ellipse(position, nsig * width, nsig * height, angle, **kwargs))
        
def plot_gmm(gmm, X, label=True, ax=None):
    ax = ax or plt.gca()
    labels = gmm.fit(X).predict(X)
    if label:
        ax.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap='viridis', zorder=2)
    else:
        ax.scatter(X[:, 0], X[:, 1], s=40, zorder=2)
    ax.axis('equal')
    
    w_factor = 0.2 / gmm.weights_.max()
    for pos, covar, w in zip(gmm.means_, gmm.covariances_, gmm.weights_):
        draw_ellipse(pos, covar, alpha=w * w_factor)

gmm = GMM(n_components=4, covariance_type='full', random_state=60)
plot_gmm(gmm, X)
plt.title("Covariance - Full")
plt.show()

gmm = GMM(n_components=4, covariance_type='diag', random_state=60)
plot_gmm(gmm, X)
plt.title("Covariance - Diag")
plt.show()

gmm = GMM(n_components=4, covariance_type='tied', random_state=60)
plot_gmm(gmm, X)
plt.title("Covariance - Tied")
plt.show()

# Chaotically Crafted by Redzwinger #


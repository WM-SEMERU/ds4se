# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/5.0_utils.clusterization.ipynb (unless otherwise specified).

__all__ = ['logger', 'CustomDistance', 'EuclideanSquareDistance', 'EuclideanDistance', 'reduce_dims_pca_tsne',
           'reduce_dims_tsne', 'reduce_dims_pca', 'get_silhouette', 'reduce_dims_umap', 'k_means', 'clusterize',
           'find_best_k', 'run_kmedoids', 'perform_clusterize_kmedoids', 'clusterize_kmedoids',
           'new_clusterize_kmedoids', 'gen_criticisms']

# Cell

import logging

import sentencepiece as sp

from pyclustering.cluster.kmedoids import kmedoids
from pyclustering.utils.metric import euclidean_distance_square, euclidean_distance
from pyclustering.cluster.silhouette import silhouette, silhouette_ksearch_type, silhouette_ksearch

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.metrics import silhouette_score, pairwise_distances_argmin_min

import umap

import numpy as np
from abc import ABC
from typing import Tuple, Optional

# Configs
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Cell

class CustomDistance(ABC):
    def compute_distance(self, x, y) -> float:
        """
        Computes the distance between 2 vectors according to a
        particular distance metric
        :param x: Vector
        :param y: Vector
        :return:
        """
        pass

# Cell

class EuclideanSquareDistance(CustomDistance):
    """Euclidean (square) distance."""
    def compute_distance(self, x, y) -> float:
        return euclidean_distance_square(x, y)

# Cell

class EuclideanDistance(CustomDistance):
    """Euclidean distance."""

    def compute_distance(self, x, y) -> float:
        return euclidean_distance(x, y)

# Cell

# Uses PCA first and then t-SNE
def reduce_dims_pca_tsne(feature_vectors, dims = 2):
    """
    """
    # hyperparameters from https://towardsdatascience.com/visualising-high-dimensional-datasets-using-pca-and-t-sne-in-python-8ef87e7915b
    pca = PCA(n_components=50)
    pca_features = pca.fit_transform(feature_vectors)
    logging.info("Reduced dims via PCA.")

    tsne = TSNE(n_components=dims, verbose=1, perplexity=40, n_iter=300)
    tsne_features = tsne.fit_transform(pca_features)
    logging.info("Reduced dims via t-SNE.")

    return tsne_features

# Cell

def reduce_dims_tsne(vectors, dims=2):
    """
    Perform dimensionality reduction using t-SNE (from sklearn)
    :param vectors: Data vectors to be reduced
    :param dims: Optional[int] indicating the number of dimensions of the desired space

    :return: Vectors with the desired dimensionality
    """
    tsne = TSNE(n_components=dims, verbose=1, perplexity=40, n_iter=300)
    tsne_feats = tsne.fit_transform(vectors)

    logging.info("Reduced dims via t-SNE")

    return tsne_feats

# Cell

def reduce_dims_pca(vectors, dims=2):
    """
    Perform dimensionality reduction using PCA (from sklearn)
    :param vectors: Data vectors to be reduced
    :param dims: Optional[int] indicating the number of dimensions of the desired space

    :return: Vectors with the desired dimensionality
    """
    pca = PCA(n_components=dims)
    pca_feats = pca.fit_transform(vectors)
    logging.info("Reduced dims via PCA.")

    return pca_feats

# Cell

def get_silhouette(samples1, samples2):
    cluster1, medoid_id1, kmedoid_instance1 = run_kmedoids(samples1, 1)
    cluster2, medoid_id2, kmedoid_instance12 = run_kmedoids(samples2, 1)
    cluster2 = np.array([[len(samples1) + x for x in cluster2[0]]])
    samples = np.concatenate((samples1, samples2), axis=0)
    clusters = np.concatenate((cluster1, cluster2), axis=0)
    score = sum(silhouette(samples, clusters).process().get_score()) / len(samples)

    return score

# Cell

def reduce_dims_umap(vectors, n_neighbors: Optional[int]=15,
                     min_dist: Optional[float]=0.1, dims: Optional[int]=2,
                     metric: Optional[str]='euclidean') -> np.ndarray:
    """
    Perform dimensionality reduction using UMAP
    :param vectors: Data vectors to be reduced
    :param dims: Optional[int] indicating the number of dimensions of the desired space

    :return: Vectors with the desired dimensionality
    """

    reducer = umap.UMAP(
        n_neighbors=n_neighbors,
        min_dist=min_dist,
        n_components=dims,
        metric=metric
    )

    umap_vectors = reducer.fit_transform(vectors)
    return umap_vectors

# Cell
def k_means(feature_vectors, k_range=[2, 3]):
    # finding best k
    bst_k          = k_range[0]
    bst_silhouette = -1
    bst_labels     = None
    bst_centroids  = None
    bst_kmeans     = None
    for k in k_range:
        kmeans = KMeans(n_clusters = k)
        kmeans.fit(feature_vectors)

        labels    = kmeans.predict(feature_vectors)
        centroids = kmeans.cluster_centers_

        silhouette_avg = silhouette_score(feature_vectors, labels)
        if silhouette_avg > bst_silhouette:
            bst_k          = k
            bst_silhouette = silhouette_avg
            bst_labels     = labels
            bst_centroids  = centroids
            bst_kmeans     = kmeans
    logger.info(f'Best k = {bst_k} with a silhouette score of {bst_silhouette}')

    centroid_mthds = pairwise_distances_argmin_min(bst_centroids, feature_vectors)
    return bst_labels, bst_centroids, bst_kmeans, centroid_mthds

# Cell

def clusterize(feature_vecs, k_range = [2], dims = 2):
    # feature_vectors = reduce_dims(np.array(list(zip(*feature_vecs))[1]), dims = dims)
    feature_vectors = reduce_dims_umap(np.array(list(zip(*feature_vecs))[1]), dims=dims)
    experimental_vectors = feature_vectors#[:len(feature_vectors) * 0.1]
    labels, centroids, kmeans, centroid_mthds = k_means(experimental_vectors, k_range = k_range)
    return (feature_vectors, centroid_mthds, labels, centroids, kmeans)

# Cell

def find_best_k(samples):
    logging.info("Searching best k for clustering.")
    search_instance = silhouette_ksearch(samples, 2, 10, algorithm=silhouette_ksearch_type.KMEDOIDS).process()
    amount = search_instance.get_amount()
    scores = search_instance.get_scores()

    logging.info(f"Best Silhouette Score for k = {amount}: {scores[amount]}")

    return amount

# Cell
def run_kmedoids(samples, k):
    initial_medoids = list(range(k))
    # Create instance of K-Medoids algorithm.
    kmedoids_instance = kmedoids(samples, initial_medoids)
    kmedoids_instance.process()
    clusters = kmedoids_instance.get_clusters()
    medoid_ids = kmedoids_instance.get_medoids()

    return clusters, medoid_ids, kmedoids_instance

# Cell

def perform_clusterize_kmedoids(data: np.array, reduct_dist='euclidean', dims: int = 2) -> Tuple:
    """
    Perform clusterization of the dataset by means of k-medoids

    :param data: Data to be clusterized
    :param reduct_dist: Distance metric to be used for dimensionality reduction
    :param dims: Number of dims to get with umap before clustering

    :return: Tuple (reduced_vectors, clusters, medoid_ids, pyclustering kmedoids instance)
    """
    reduced_data = reduce_dims_umap(data, dims = dims)
    k = find_best_k(reduced_data)

    clusters, medoid_ids, kmedoids_instance = run_kmedoids(reduced_data, k)

    return reduced_data, clusters, medoid_ids, kmedoids_instance

# Cell

def clusterize_kmedoids(data: np.array, distance_metric='euclidean', dims: int = 2) -> Tuple:
    """
    Performs clusterization (k-medoids) using UMAP for dim. reduction
    """
    reduced_data = reduce_dims_umap(data, dims = dims, metric=distance_metric)
    logging.info('Reduced dimensionality via UMAP')
    k = find_best_k(reduced_data)

    clusters, medoid_ids, kmedoids_instance = run_kmedoids(reduced_data, k)

    return reduced_data, clusters, medoid_ids, kmedoids_instance

# Cell
def new_clusterize_kmedoids(h_samples, m1_samples, m2_samples, m3_samples, dims = 2):
    samples = np.concatenate((h_samples, m1_samples, m2_samples, m3_samples), axis=0)
    samples = reduce_dims(samples, dims = dims) # np.array(list(zip(*samples)))[0], dims = dims)
    h_samples, m1_samples, m2_samples, m3_samples = samples[:len(h_samples)], samples[len(h_samples):len(h_samples) + len(m1_samples)], samples[len(h_samples) + len(m1_samples):len(h_samples) + len(m1_samples) + len(m2_samples)], samples[len(h_samples) + len(m1_samples) + len(m2_samples):]
    h_k = find_best_k(h_samples)
    h_clusters, h_medoid_ids, h_kmedoids_instance = run_kmedoids(h_samples, h_k)
    m1_k = find_best_k(m1_samples)
    m1_clusters, m1_medoid_ids, m1_kmedoids_instance = run_kmedoids(m1_samples, m1_k)
    m2_k = find_best_k(m2_samples)
    m2_clusters, m2_medoid_ids, m2_kmedoids_instance = run_kmedoids(m2_samples, m2_k)
    m3_k = find_best_k(m3_samples)
    m3_clusters, m3_medoid_ids, m3_kmedoids_instance = run_kmedoids(m3_samples, m3_k)

    return (
        (h_samples, h_clusters, h_medoid_ids, h_kmedoids_instance),
        (m1_samples, m1_clusters, m1_medoid_ids, m1_kmedoids_instance),
        (m2_samples, m2_clusters, m2_medoid_ids, m2_kmedoids_instance),
        (m3_samples, m3_clusters, m3_medoid_ids, m3_kmedoids_instance)
    )

# Cell

def gen_criticisms(samples, prototypes, n = None, distance = None):
    if n is None: n = len(prototypes)
    if distance is None:
        distance = EuclideanDistance()
    crits = []
    for x in samples:
        mean_dist_x = 0.
        for x_i in samples:
            mean_dist_x += distance.compute_distance(x, x_i)
        mean_dist_x = mean_dist_x / len(x)

        mean_dist_proto = 0.
        for z_j in prototypes:
            mean_dist_proto += distance.compute_distance(x, z_j)
        mean_dist_proto = mean_dist_proto / len(prototypes)

        crits.append(mean_dist_x - mean_dist_proto)

    crits = np.array(crits)
    crit_ids = crits.argsort()[-n:][::-1]

    return crits, crit_ids
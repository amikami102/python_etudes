# kmeans.py
"""
A script implementing k-means clustering with standard built-in Python libraries.

1. Specify the number of clusters you want. Call this number `k`.
2. Normalize the data points.
3. Create k random centroids, one for each cluster.
4. Assign each data point to the cluster of the centroid it is closest to.
5. Recalculate each centroid so that it is the mean of the cluster it is associated with.
6. Repeat steps 4 and 5 until the maximum number of iterations is reached or the centroids stop moving (convergence).
"""
from typing import *
from copy import deepcopy
import functools
import random
from statistics import pvariance, pstdev, mean
from dataclasses import dataclass

from rich import print

from data_point import DataPoint


P = TypeVar('Point', bound=DataPoint)


def zscores(data: Sequence[float]) -> Sequence[float]:
    """ Compute z-scores of sample data. """
    if pvariance(data) == 0:
        raise ValueError('No variance in the data')
    else:
        mu: float = mean(data)
        sigma: float = pstdev(data)
        return [
            (x-mu)/sigma for x in data
        ]
    

class KMeans(Generic[P]):
    
    @dataclass
    class Cluster:
        """ A dataclass to keep track of each class in the operation. """
        points: list[P]
        centroid: DataPoint
    
    
    def __init__(self, k: int, points: list[P]) -> None:
        if k < 1:
            raise ValueError("k must be at least 1")
        
        self.k: int = k
        self._points: list[P] = points
        self.n_dimensions: int = next(iter(self._points)).num_dimensions
        self._zscore_normalize()
        
        self._clusters: list[KMeans.Cluster] = [
            KMeans.Cluster([], self._random_point())
            for _ in range(k)
        ]
        
    @property
    def _centroids(self) -> list[DataPoint]:
        """ Return the centroids of clusters. """
        return [x.centroid for x in self._clusters]
    
    def _dimension_slice(self, dimension: int) -> list[float]:
        """ Return a dimension of data. """
        return [ x.dimensions[dimension] for x in self._points]
    
    def _zscore_normalize(self) -> None:
        """ Replace the values in `dimensions` of each data point with its z-scored equivalent. """
        # calculate z-score per dimension
        zscored: list[list[float]] = [
            zscore([x.dimensions[p] for x in self._points])
            for p in range(self.n_dimensions)
        ]
        for i, datapoint in enumerate(self._points):
            datapoint.dimensions = tuple(zscored[p][i] for p in range(n_dimensions))
    
    def _random_point(self) -> DataPoint:
        """ Create random Data Point that can be used for initial centroids. """
        rand_dimensions: list[float] = []
        
        for p in range(self.n_dimensions):
            values: list[float] = [x.dimensions[p] for x in self._points]
            rand_value: float = random.uniform(min(values), max(values))
            rand_dimensions.append(rand_value)
        
        return DataPoint(rand_idmensions)

    def _assign_cluster(self) -> None:
        """ Find the closest cluster centroid for each data point and assign the data point to that cluster. """
        for point in self._points:
            closest: DataPoint = min(self._centroids, key=functools.partial(DataPoint.distance, point))
            cluster: KMeans.Cluster = self._clusters[self._centroids.index(closest)]
            cluster.points.append(point)
    
    def _generate_centroids(self) -> None:
        """ Find the center of each cluster and move the centroid to there. """
        for cluster in self._clusters:
            if not cluster.points:
                continue # keep the same centroid if no point has been assigned to this cluster
            else:
                dim_means: list[float] = [
                    mean(point.dimensions[p] for point in cluster.points)
                    for p in range(self.n_dimensions)
                ]
                cluster.centroid = DataPoint(dim_means)
    
    def run(self, max_iter: int = 100) -> list[Kmeans.Cluster]:
        """ Run k-means clustering until convergence has been reached or max number of iterations have been run. """
        for i in range(max_iter):
            for cluster in self._clusters:
                cluster.points.clear()				# clear all clusters
            self._assign_clusters()					# find cluster each point is closest to
            old_centroids: list[DataPoint] = deepcopy(self._centroids)
            self._generate_centroids()				# find new centroids
            if old_centroids == self._centroids:	# check for convergence
                print("Converged after {i} iterations")
                return self._clusters
        
        return self._clusters
    
    
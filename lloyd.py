from utils import manhattan_distance, euclidean_distance
from matplotlib import pyplot as plt
import numpy as np
import random


def nearest_centroid(point, centroids, distance):
    dst_lst = [distance(point, x) for x in centroids]
    idx = np.argmin(np.array(dst_lst))
    return (idx, dst_lst[idx])


def lloyd(data, k, iters, _type, distance):
    
    if distance == "euclidean":
        distance = euclidean_distance
    elif distance == "manhattan":
        distance = manhattan_distance

    centroid_idx = random.sample(range(len(data)), k)
    centroids = [data[idx] for idx in centroid_idx]
    error = 0

    for it in range(iters):
        n_centroids = [[] for _ in range(k)]
        errors = []

        # Sort de los puntos en clusters
        for point in data:
            idx, dst = nearest_centroid(point, centroids, distance)
            n_centroids[idx].append(point)
            errors.append(dst)

        # Calculo del error
        n_error = np.sum(np.array(errors))

        for idx, centroid in enumerate(n_centroids):
            if _type == "means":
                centroids[idx] = np.array(centroid).mean(axis=0)

            if _type == "medioids":
                centroids[idx] = np.array(centroid).median()

        #print(centroids)
        error = n_error

    return {"Centroids":centroids, "Error": error}
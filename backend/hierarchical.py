#!/usr/bin/python3
from pearson import *

class Cluster(dict):
    """
    This class creates a subclass of dict and uses itself as the underlying __dict__ of the instance.
    This is to be able to serialize it and send as a tree to the frontend.
    """
    def __init__(self, blog, left=None, right=None, distance=0.0,id=None):
        super().__init__()
        self.__dict__ = self
        self.blog = blog
        self.left = left
        self.right=right
        self.id = id
        self.distance = distance


def createClusters(data):
    """
    Create clusters
    """
    # Start by generating one cluster for each blog
    clusters = [] # list of dictionaries
    # print(len(data)) # 99
    # 99 blogs with a vector of 706 wordcounts
    #for blog in data:
    for i in range(0, len(data)):
        # Create a list of objects/clusters
        clusters.append(Cluster(data[i], id = i))
    return clusters


def hierarchical(clusters):
    """Hierarchy generation algorithm.

    @param data list of lists (a vector of wordcounts for each blog)
    """
    distances = {}
    currentClustid = -1
    count = 0
    while (len(clusters) > 1):
        lowestPair = (0,1)
        count += 1
        print('Iteration nr #' + str(count))
        print('Nr of clusters: ' + str(len(clusters)))
        closest = pearson(clusters[0].blog, clusters[1].blog)

        # loop through every blog pair
        # and search for smallest distance
        for i in range(0, len(clusters)):
            # ( i + 1 ) because we leave the blog
            # we are comparing with out
            for j in range(i+1, len(clusters)):
                # cache distances in dict
                # use id's to tag blog pairs f.ex (0,1) etc
                if (clusters[i].id, clusters[j].id) not in distances:
                    distances[(clusters[i].id, clusters[j].id)] = pearson(clusters[i].blog, clusters[j].blog)

                d = distances[(clusters[i].id, clusters[j].id)]

                if d < closest:
                    closest = d
                    lowestPair = (i,j)
        # calculate the average of the two clusters

        mergeBlogs = []
        for i in range(0, len(clusters[0].blog)):
            avg = clusters[lowestPair[0]].blog[i] + clusters[lowestPair[1]].blog[i] / 2
            avg = round(avg, 4)
            mergeBlogs.append(avg)

        #create the new cluster
        newCluster = Cluster(
            mergeBlogs, left=clusters[lowestPair[0]], right=clusters[lowestPair[1]],
            distance=round(closest, 4),
            id=currentClustid
            )

        # cluster ids that werent in the original set are negative

        currentClustid -= 1

        del clusters[lowestPair[1]]
        del clusters[lowestPair[0]]
        clusters.append(newCluster)

    return clusters[0]


def printLeafNodes(cluster, blognames, tab=" "):
    """
    Recursive function to print tree
    """


    # if node is null, return
    if (cluster is None):
        return

    print("folder")

    # If node is leaf node, print its data
    if (cluster.left is None and cluster.right is None):
        tab += " "
        print("\n" + tab + blognames[cluster.id] + " " + str(cluster.distance))
        return

    # If left child exists, check for leaf recursively
    if (cluster.left):
        print("left")
        printLeafNodes(cluster.left, blognames, tab)

    # If right child exists, check for leaf recursively
    if (cluster.right):
        print("right")
        printLeafNodes(cluster.right, blognames, tab)

        #print(blognames[cluster.right.id])




# def iterate(clusters, count):
#     """
#     Iterate as long as there is more than one cluster
#     in the clusters list
#     """
#     closest = 1000
#     A = {}
#     B = {}
#     # iterate through the clusters
#     for clusterA in clusters:
#         # for each cluster, calculate distance to the other clusters
#         for clusterB in clusters:
#             distance = pearson(clusterA['blog'], clusterB['blog'])
#             if (distance < closest and clusterA != clusterB):
#                 closest = distance
#                 A = clusterA
#                 B = clusterB
#     # Merge the two clusters
#     C = merge(A, B, closest)
#     clusters.append(C)
#     # Remove old clusters
#     clusters.remove(A)
#     clusters.remove(B)
#     # clusters.remove(A)
#     # clusters.remove(B)
#
#     return clusters, count
#
#
# def merge(clusterA, clusterB, distance):
#     """
#     Merge two clusters A and B
#     """
#     # Create a new cluster
#     clusterP = {}
#     # Fill data
#     clusterP['left'] = clusterA
#
#     clusterP['right'] = clusterB
#
#
#     nrOfWords = 706
#     # merge blog data by averaging word counts for each word
#     #mergedBlog = {'words': []}
#     newBlog = []
#     #for i in range(0, 705):
#     for i in range(0, len(clusterB['blog']) ):
#         wordA = clusterA['blog'][i]
#         wordB = clusterB['blog'][i]
#         #print("wordA: " + str(wordA))
#         #print("wordB: " + str(wordB))
#         count = (wordA + wordB) / 2
#         #mergedBlog['words'] = (wordA, count)
#         # testing this: just add average count for each word in the two merged blogs, in a vector/list
#         #mergedBlog['words'].append(count)
#         newBlog.append(count)
#
#
#     #print(len(clusterB['blog']))
#     # Set blog to new cluster
#     #clusterP['blog'] = mergedBlog['words']
#     clusterP['blog'] = newBlog
#     # Set distance
#     clusterP['distance'] = distance
#     #clusterA['parent'] = clusterP
#     #clusterB['parent'] = clusterP
#
#     # Return new cluster
#     return clusterP

import random
from pearson import pearson


def kcluster(rows, nrOfClusters=4, nrOfIterations=99):
    """
    Start with a number of randomly placed clusters
    rows = the rows in the data set
    Data Set contains word frequencies in blogs
    rows[0] = The first row is the words
    """
    # Determine the min and max wordcount for each word
    # ranges = [(min([row[i] for row in rows]), max([row[i] for row in rows])) for i in range(len(rows[0]))]

    ranges = []

    # a loop which runs 706 times (the number of words)
    for i in range(len(rows[0])):
        # 706 words for each row/blog
        tempwcs = []
        for row in rows:
            tempwcs.append(row[i])
        minimum = min(tempwcs)
        maximum = max(tempwcs)
        ranges.append((minimum,maximum))

    # clusters = [[random.random()*(ranges[i][1]-ranges[i][0])+ranges[i][0] for i in range(len(rows[0]))] for j in range(nrOfClusters)]

    # Create nrOfClusters randomly placed centroids
    clusters = []
    # Loop through nrOfClusters specified
    for j in range(nrOfClusters):
        cluster = []
        # Create a loop that runs 706 times
        for i in range(len(rows[0])):
            # get random float between min and max (for each word)
            cluster.append(random.uniform(ranges[i][0], ranges[i][1]))
        clusters.append(cluster)

# Each centroid will have 706 randomly generated counts
# ranging from min to max for that specific word

    lastmatches = None

    for t in range(nrOfIterations):
        print('Iteration %d' % t)
        # create a list of nrOfIterations empty lists
        bestmatches=[[] for i in range(nrOfClusters)]

        # Find which centroid is the closest for each row/blog
        for j in range(len(rows)):
            row = rows[j]
            # create var to place the best match
            bestmatch = 0
            for i in range(nrOfClusters):
                # Get distance for each blog compared to cluster
                d = pearson(clusters[i], row)
                # Compare to former best match
                if d < pearson(clusters[bestmatch], row):
                    #assign best match if true
                    bestmatch=i
            # create tuple to also return assignments
            bestmatches[bestmatch].append(j)

        # If the results are the same as last time, this is complete
        if bestmatches==lastmatches: break
        lastmatches=bestmatches

        # Move the centroids to the average of their members
        for i in range(nrOfClusters):
            # Create list of 0.0 of length 706 (words)
            avgs= [0.0] * len(rows[0])
            if len(bestmatches[i]) > 0:
                # Loop through each cluster's blogid/row_nr
                for rowid in bestmatches[i]:
                    for m in range(len(rows[rowid])):
                        avgs[m] += rows[rowid][m]
                for j in range(len(avgs)):
                    avgs[j] /= len(bestmatches[i])
                clusters[i]=avgs

    return bestmatches

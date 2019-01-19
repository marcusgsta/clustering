from math import sqrt

def pearson(user1, user2):
    """
    @param list
    @param list
    Compares two lists
    returns a pearson correlation coefficient
    between 0 and 1
    """
    #print(len(user1))
    #print(len(user2))
    # Sum of each user's ratings
    sum1 = sum(user1)
    sum2 = sum(user2)

    # Loop through each array of values
    # Each value squared
    # Save the sum of the squared values
    sum1Sq = sum([pow(user,2) for user in user1])
    sum2Sq = sum([pow(user,2) for user in user2])

    # Loop through the ratings and multiply with each other
    # Get total
    pSum = 0
    for i in range(len(user1)):
        pSum += user1[i] * user2[i]


    # Calculate r (Pearson score)
    # algorithm: num = pSum - (sum1*sum2/n)
    # n = number of movies both users have rated
    num = pSum - (sum1 * sum2 / len(user1))

    # algorithm: den = sqrt( (sum1sq - pow(sum1,2)/n) * (sum2sq - pow(sum2sq)/n)
    # r = num / den

    den = sqrt(( sum1Sq-pow(sum1,2) / len(user1)) * (sum2Sq-pow(sum2,2) / len(user1) ))

    if den == 0: return 0

    # 1 - pearson correlation, to return smaller distance between items that are more similar
    return 1.0 - num/den

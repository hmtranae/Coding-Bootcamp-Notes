def sockMerchant(n, ar):
    """
    Input: integer n represents the number of socks in array ar
    ar contains n space-separated integers describing the colors ar[i] of socks in the pile
    Returns total number of matching socks
    """
    sockSet = set()
    countMatch = 0
    for i in ar:
        if i in sockSet:
            countMatch += 1
            sockSet.discard(i)
        else:
            sockSet.add(i)
    return countMatch
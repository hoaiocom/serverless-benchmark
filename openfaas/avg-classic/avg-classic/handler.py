def avg(arr):
    n = len(arr)
    sum = 0
    # Traverse through all array elements
    for i in range(n):
        sum = sum + arr[i]
    return sum/n

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    x = [int(i) for i in req.split(",")]
    result=avg(x)

    return str(result)
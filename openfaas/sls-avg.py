def avg(arr):
    n = len(arr)
    sum = 0
    # Traverse through all array elements
    for i in range(n):
        sum = sum + arr[i]
    return sum/n

def handle(event, context):
    if event.method == 'POST':
        x = [int(i) for i in str(event.body,'utf-8').split(",")]
        return {
            "statusCode": 200,
            "body": avg(x)
        }
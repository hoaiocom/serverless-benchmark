from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

def bubbleSort(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

class BubbleSort(Resource):
    def post(self):
        args = [int(i) for i in str(request.data,'utf-8').split(",")]
        result = bubbleSort(args)
        return result

api.add_resource(BubbleSort, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port="8081")
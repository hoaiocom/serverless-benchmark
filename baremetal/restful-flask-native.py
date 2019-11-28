from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

def avg(arr):
    n = len(arr)
    sum = 0
    # Traverse through all array elements
    for i in range(n):
        sum = sum + arr[i]
    return sum/n

def merge_sort(arr):
    # The last array split
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    # Perform merge_sort recursively on both halves
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    # Merge each side together 
    return merge(left, right, arr.copy())

def merge(left, right, merged):

    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):

        # Sort each one and place into the result
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor+right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]
    return merged

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

class Avg(Resource):
    def post(self):
        args = [int(i) for i in str(request.data,'utf-8').split(",")]
        result = avg(args)
        return jsonify(result)

class Merge(Resource):
    def post(self):
        args = [int(i) for i in str(request.data,'utf-8').split(",")]
        result = merge_sort(args)
        return jsonify(result)

class Bubble(Resource):
    def post(self):
        args = [int(i) for i in str(request.data,'utf-8').split(",")]
        result = bubbleSort(args)
        return jsonify(result)

api.add_resource(Avg, '/avg')
api.add_resource(Merge, '/merge')
api.add_resource(Bubble, '/bubble')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port="8000")
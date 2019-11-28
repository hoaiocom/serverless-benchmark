from flask import Flask, request, jsonify

app = Flask(__name__)

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

@app.route("/")
def main():
    return jsonify("Hello World")

@app.route("/avg", methods=['POST'])
def avg_f():
    args = [int(i) for i in str(request.data,'utf-8').split(",")]
    result = avg(args)
    return jsonify(result)

@app.route("/merge", methods=['POST'])
def merge_f():
    args = [int(i) for i in str(request.data,'utf-8').split(",")]
    result = merge_sort(args)
    return jsonify(result)

@app.route("/bubble", methods=['POST'])
def bubble_f():
    args = [int(i) for i in str(request.data,'utf-8').split(",")]
    result = bubbleSort(args)
    return jsonify(result)
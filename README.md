# Serverless-benchmark
Snippets for simple benchmarking and comparing between Serverless and Bare metal
# Benchmark Testing
* Github: [https://github.com/itbiboo/serverless-benchmark](https://github.com/itbiboo/serverless-benchmark)
## Bare Metal
Using Flask-Restful API
1. Create Virtual Environment
	```go
	virtualenv <environment>
	```
	Active environment
	```go
	source avg/bin/activate
	```
	Deactive
	```go
	deactive
	```
2. Install flask and flask-restful via pip3
	```bash
	pip3 install flask
	pip3 install flask-restful
	```
3. Run API
	```bash
	python3 api.py
	```
### Average
```bash
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

class Avg(Resource):
    def get(self):
        return {'hello': 'world'}
    def post(self):
        args = [int(i) for i in str(request.data,'utf-8').split(",")]
        result = avg(args)
        return result

api.add_resource(Avg, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port="8082")
```
### Bubble sort
```bash
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
    def get(self):
        return {'hello': 'world'}
    def post(self):
        args = [int(i) for i in str(request.data,'utf-8').split(",")]
        result = bubbleSort(args)
        return result

api.add_resource(BubbleSort, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port="8081")
```
### Merge sort
```python
from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# Main code
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

class MergeSort(Resource):
    def get(self):
        return {'hello': 'world'}
    def post(self):
        args = [int(i) for i in str(request.data,'utf-8').split(",")]
        result = merge_sort(args)
        return result

api.add_resource(MergeSort, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port="8080")
```

### Testing with Hey
```bash
hey -m POST -d "88620, 80669, 59890, 41088, 32813, 36151, 46272, 74514, 48791, 47899, 33063, 2915, 46979, 35634, 93588, 30155, 68587, 91453, 26021, 51667, 69944, 90409, 28718, 64454, 15618, 10349, 73925, 31975, 2803, 7861, 87344, 59671, 70812, 92323, 83702, 81189, 96576, 44812, 99301, 52890, 32562, 9815, 68855, 61486, 36960, 59695, 15690, 21418, 73461, 79011, 44677, 70549, 12301, 55668, 69644, 70229, 64458, 21100, 18274, 38967, 31127, 6379, 24217, 61478, 2000, 26522, 85477, 89131, 45277, 59071, 32037, 26479, 54861, 41129, 50963, 84814, 64504, 14340, 3728, 68432, 44444, 90104, 27149, 81245, 35594, 44910, 68721, 43675, 50397, 92581, 38489, 32145, 69620, 62523, 51588, 16753, 61666, 81980, 23224, 58959" http://127.0.0.1:8080
```

Sample response
```bash
Summary:
  Total:	0.3665 secs
  Slowest:	0.1007 secs
  Fastest:	0.0062 secs
  Average:	0.0812 secs
  Requests/sec:	545.6624
  
  Total data:	138800 bytes
  Size/request:	694 bytes

Response time histogram:
  0.006 [1]	|■
  0.016 [5]	|■■■
  0.025 [3]	|■■
  0.035 [5]	|■■■
  0.044 [5]	|■■■
  0.053 [6]	|■■■
  0.063 [4]	|■■
  0.072 [7]	|■■■■
  0.082 [10]	|■■■■■
  0.091 [74]	|■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.101 [80]	|■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


Latency distribution:
  10% in 0.0463 secs
  25% in 0.0832 secs
  50% in 0.0900 secs
  75% in 0.0929 secs
  90% in 0.0948 secs
  95% in 0.0956 secs
  99% in 0.0974 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0014 secs, 0.0062 secs, 0.1007 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0000 secs
  req write:	0.0001 secs, 0.0000 secs, 0.0006 secs
  resp wait:	0.0790 secs, 0.0028 secs, 0.0969 secs
  resp read:	0.0006 secs, 0.0000 secs, 0.0038 secs

Status code distribution:
  [200]	200 responses
```
### Measure CPU
Using psrecord
```bash
pip install psrecord
```
Record CPU and memory and plot
```bash
psrecord 1330 --log activity.txt --plot plot.png
```
Detail: [https://github.com/itbiboo/psrecord](https://github.com/itbiboo/psrecord)

## Serverless - OpenFaaS

### Get template
Using of-watchdog [https://github.com/openfaas-incubator/of-watchdog](https://github.com/openfaas-incubator/of-watchdog)
```bash
faas-cli template pull https://github.com/openfaas-incubator/python-flask-template
```
Check
```bash
 faas-cli new --list
```
### Create new project
Create new project
```bash
faas-cli new --lang <language-name> <funtions-name> --prefix="<your-docker-username-here>"
```

Sample handle.py
```bash
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
```

### Build, deploy and push
```bash
faas-cli up -f <yml file>
```


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
hey -m POST -d "64955, 97434, 8377, 48956, 33303, 18756, 91915, 42406, 33838, 41183, 116, 7738, 17952, 71340, 60153, 31376, 52195, 19090, 94206, 30076, 11687, 59126, 37705, 83522, 11462, 55720, 42745, 25401, 80675, 5577, 90951, 38792, 50730, 2477, 61681, 1694, 24850, 17851, 23872, 53447, 74686, 74254, 44111, 98762, 26544, 21295, 73640, 47008, 69594, 50697, 80140, 6061, 76665, 12167, 80530, 33343, 47926, 42293, 73123, 97614, 46644, 89111, 65356, 26858, 55330, 64253, 89736, 14162, 88531, 82828, 2489, 65264, 83995, 16480, 66774, 81089, 3268, 84845, 34283, 7801, 61892, 78947, 65503, 48922, 78804, 40938, 41108, 57252, 41237, 46335, 34228, 59189, 63970, 53943, 37284, 31821, 15376, 68168, 73072, 39290, 71056, 30647, 82954, 20523, 12083, 65598, 45553, 49856, 69828, 57717, 3816, 78331, 20326, 46042, 20739, 17748, 48950, 8392, 26704, 28388, 84223, 12034, 79702, 32298, 27251, 8621, 97494, 62638, 30094, 41890, 64778, 65358, 86614, 50301, 86228, 34335, 21319, 38980, 86551, 14809, 70072, 23651, 34976, 47917, 25503, 72558, 8555, 72994, 57311, 2153, 65545, 39795, 18259, 72117, 25063, 73543, 16741, 621, 15683, 73426, 80698, 7859, 91845, 5537, 2798, 17220, 77270, 12402, 72820, 95841, 80138, 20059, 69640, 44445, 89605, 71934, 40878, 36656, 66999, 15457, 66910, 35193, 84234, 45297, 5929, 3728, 63453, 68288, 92251, 83867, 27002, 13113, 10332, 46336, 8333, 21408, 38673, 36524, 87088, 86499, 82338, 93155, 21887, 55490, 9990, 33101, 41131, 87149, 80337, 72805, 3378, 5048, 4413, 98587, 35763, 49270, 17474, 85310, 16768, 44829, 39807, 74115, 61527, 41705, 89824, 72596, 62557, 38682, 25002, 29043, 2856, 29309, 67152, 73442, 31121, 99045, 58828, 43791, 83190, 20857, 36387, 88536, 51305, 97693, 66113, 36553, 92856, 54215, 16572, 9606, 46113, 75468, 19385, 56154, 16120, 17817, 5890, 5859, 65809, 20672, 13814, 16636, 97021, 42636, 74211, 66307, 4316, 37676, 32250, 17526, 6284, 27026, 56979, 93661, 91742, 98653, 50154, 76810, 69462, 68581, 67154, 79822, 78699, 66615, 67567, 65005, 9940, 41080, 53600, 34426, 76454, 80119, 3554, 15186, 3363, 59412, 49711, 19506, 37429, 74791, 74847, 87222, 11598, 68983, 22805, 82721, 55892, 7826, 62458, 82263, 16744, 25433, 14978, 71486, 14734, 19682, 33166, 15017, 11359, 24933, 88143, 53835, 12530, 95709, 27624, 68806, 44800, 58220, 87446, 69797, 16433, 53064, 66180, 11680, 34777, 56386, 11683, 78150, 32976, 66150, 31854, 95220, 39122, 74876, 93742, 67546, 93618, 84120, 94549, 2763, 17137, 21686, 58226, 51211, 47542, 73619, 19661, 97437, 77, 63928, 48228, 83366, 47037, 60103, 52105, 82124, 44250, 47649, 60102, 98704, 84778, 63420, 48254, 65964, 4857, 33221, 90117, 94301, 98293, 59424, 76079, 56949, 18315, 77536, 4113, 26212, 3140, 81701, 87008, 60925, 95377, 97955, 43447, 61052, 12002, 73819, 72976, 41736, 72983, 82158, 67161, 2872, 56875, 81699, 26259, 10931, 27678, 27167, 6157, 93705, 55331, 3383, 16157, 90502, 81369, 67992, 53511, 69320, 64080, 23009, 73330, 15232, 51354, 98408, 86296, 54742, 36081, 20098, 42555, 97064, 64113, 5828, 28764, 16349, 39219, 85454, 95305, 10819, 44913, 59215, 54077, 53818, 32383, 301, 1026, 3148, 80451, 63501, 64048, 30960, 9441, 23835, 75676, 65616, 39085, 43538, 40571, 46396, 96172, 68011, 16092, 62003, 98990, 26469, 55920, 89469, 99180, 86023, 59281, 55599, 90869, 13737, 50868, 78340, 50068, 65706, 12386, 74264, 4073, 75734, 777, 93898, 94870, 20980, 41404, 66534, 74979, 88901, 55588, 93959, 34752, 63985, 59622, 28147, 15685, 21086, 32668, 69253, 61205, 3576, 73041, 83732, 66515, 5649, 39206, 66894, 51575, 46141, 77238, 47132, 48952, 54236, 42339, 10166, 65240, 1095, 5894, 67133, 5376, 81146, 41801, 15438, 31222, 51736, 4993, 97098, 51817, 31396, 85935, 83795, 69221, 41456, 42975, 93417, 88617, 51169, 82396, 647, 50400, 35947, 80437, 23501, 36876, 12782, 96740, 15047, 69426, 77543, 3082, 41081, 55086, 57617, 97327, 23555, 96317, 24071, 46745, 96534, 56524, 39684, 79222, 37168, 82169, 62059, 92583, 5103, 99918, 29557, 30064, 84558, 19897, 75634, 73189, 55275, 44720, 59802, 45120, 91045, 97055, 35425, 35450, 64528, 16760, 94448, 12714, 48298, 64951, 70010, 55418, 12277, 70615, 81165, 69373, 85208, 96037, 47985, 76353, 88660, 30514, 40638, 10763, 88374, 64626, 15936, 92659, 19560, 39878, 93062, 46639, 60651, 40137, 79501, 71259, 69644, 83455, 76025, 86024, 30269, 4453, 14392, 68915, 98553, 29519, 18659, 97538, 77789, 87016, 25859, 28209, 83427, 64878, 94899, 89298, 41101, 23079, 66057, 19865, 9810, 28283, 69793, 84531, 61272, 36011, 4880, 76350, 80721, 62213, 2721, 11219, 23943, 89486, 47593, 44234, 55779, 22096, 68782, 88650, 79849, 96605, 31093, 28902, 34707, 91465, 38222, 60071, 1745, 9227, 21382, 68078, 51017, 24012, 15342, 21853, 46265, 76142, 58377, 78271, 3416, 91832, 21619, 80199, 76043, 77363, 83027, 45360, 91433, 95269, 59459, 63150, 55402, 54332, 45044, 49051, 69890, 43750, 76601, 79723, 86269, 34771, 37884, 53252, 99940, 8020, 42565, 12553, 32902, 45542, 83006, 52700, 77403, 52065, 24260, 47222, 71522, 83887, 39822, 20793, 38302, 56612, 13561, 15503, 34614, 33940, 32979, 16392, 11631, 92402, 94766, 19220, 64677, 8324, 85056, 51804, 8873, 7104, 62218, 50026, 63515, 14897, 13351, 91761, 47912, 50168, 46584, 23025, 80212, 33198, 67252, 42691, 78736, 98932, 9085, 25587, 98629, 45434, 95164, 20595, 7568, 19137, 58723, 42803, 37611, 50322, 75305, 17731, 52435, 44260, 81656, 34240, 54666, 99087, 99633, 20965, 5657, 61526, 77431, 64439, 7291, 88879, 91450, 84484, 81006, 30030, 10591, 85891, 32773, 77965, 97018, 60073, 96164, 47556, 66144, 73953, 25932, 93371, 64082, 29746, 37442, 25904, 32256, 70407, 69319, 90878, 74056, 95157, 42692, 2192, 96248, 29953, 20077, 5333, 82509, 29187, 11377, 59042, 67696, 1105, 35823, 55048, 27732, 61293, 93587, 50528, 38004, 86416, 39316, 35807, 67108, 23718, 39140, 95070, 69278, 1425, 98635, 89527, 86355, 43369, 97375, 71028, 39233, 37715, 45688, 2498, 15413, 62404, 85458, 52453, 17469, 42955, 14491, 11804, 2399, 47582, 53539, 79843, 53545, 95766, 80011, 8744, 21488, 34659, 80159, 17320, 22480, 92158, 33944, 14412, 72004, 27259, 17439, 15579, 12961, 13350, 85183, 38714, 36189, 42283, 4762, 99320, 64695, 43167, 83260, 77520, 49131, 65470, 63315, 75894, 33935, 30669, 8644, 93874, 43180, 85952, 90723, 65002, 28168, 70846, 58572, 11055, 53507, 10259, 89401, 59865, 61424, 76525, 48226, 41744, 34869, 73297, 69018, 37537, 10732, 21674, 26245, 35756, 23150, 59221, 69407, 98666, 65548, 92574, 51204, 48719, 54271, 77333, 60428, 74450, 14406, 58584, 18556, 38416, 48225, 1098, 61085, 54245, 9311, 54828, 65555, 64872, 66038, 44454, 68989, 267, 42213, 82394, 46772, 54617, 43013, 43494, 77631, 77079, 81801, 70218, 16720, 39735, 56666, 63183, 43419, 3835, 48236, 21978, 47859, 3621, 92442, 92637, 85926, 50899, 88442, 10832, 25280, 62966, 46741, 81781, 22603, 66149, 30321, 16377, 94912, 83089, 14343, 58180, 55174, 64317, 91644, 77060, 25110, 77067, 77529, 5033, 62829, 65498, 13442, 87092, 70674, 60327, 41477, 45679, 74690, 22996, 77595" http://127.0.0.1:8080
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



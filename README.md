# Simple Benchmark Testing
## Candidates
1. **Bare metal (native)**: Deploy functions (API) directly on physical server (not use virtualization)
2. **OpenFaas (serverless)**: Deploy functions using OpenFaaS platform (classic watchdog and of-watchdog)
Both deployed on same machine:
**Lenovo Legion-T730-28ICO**
_Core i9 i9-9900K - 32 GB RAM - 1 TB SSD - NVIDIA GeForce RTX 2080 8 GB, Ubuntu 16.04 64 bit_
### Algorithms use to test
1. Calculate **Average** of input numbers. Complexity: O(n)
2. **Merge sort**. Complexity: O(nlogn)
3. **Bubble Sort**. Complexity: O(n^2)
Using same algorithm and same input numbers for all test.
**Input numbers for testing** (for all cases): 1000 random numbers from 1 to 100.000, generated from random.org: file input.txt
```bash
64955, 97434, 8377, 48956, 33303, 18756, 91915, 42406, 33838, 41183, 116, 7738, 17952, 71340, 60153, 31376, 52195, 19090, 94206, 30076, 11687, 59126, 37705, 83522, 11462, 55720, 42745, 25401, 80675, 5577, 90951, 38792, 50730, 2477, 61681, 1694, 24850, 17851, 23872, 53447, 74686, 74254, 44111, 98762, 26544, 21295, 73640, 47008, 69594, 50697, 80140, 6061, 76665, 12167, 80530, 33343, 47926, 42293, 73123, 97614, 46644, 89111, 65356, 26858, 55330, 64253, 89736, 14162, 88531, 82828, 2489, 65264, 83995, 16480, 66774, 81089, 3268, 84845, 34283, 7801, 61892, 78947, 65503, 48922, 78804, 40938, 41108, 57252, 41237, 46335, 34228, 59189, 63970, 53943, 37284, 31821, 15376, 68168, 73072, 39290, 71056, 30647, 82954, 20523, 12083, 65598, 45553, 49856, 69828, 57717, 3816, 78331, 20326, 46042, 20739, 17748, 48950, 8392, 26704, 28388, 84223, 12034, 79702, 32298, 27251, 8621, 97494, 62638, 30094, 41890, 64778, 65358, 86614, 50301, 86228, 34335, 21319, 38980, 86551, 14809, 70072, 23651, 34976, 47917, 25503, 72558, 8555, 72994, 57311, 2153, 65545, 39795, 18259, 72117, 25063, 73543, 16741, 621, 15683, 73426, 80698, 7859, 91845, 5537, 2798, 17220, 77270, 12402, 72820, 95841, 80138, 20059, 69640, 44445, 89605, 71934, 40878, 36656, 66999, 15457, 66910, 35193, 84234, 45297, 5929, 3728, 63453, 68288, 92251, 83867, 27002, 13113, 10332, 46336, 8333, 21408, 38673, 36524, 87088, 86499, 82338, 93155, 21887, 55490, 9990, 33101, 41131, 87149, 80337, 72805, 3378, 5048, 4413, 98587, 35763, 49270, 17474, 85310, 16768, 44829, 39807, 74115, 61527, 41705, 89824, 72596, 62557, 38682, 25002, 29043, 2856, 29309, 67152, 73442, 31121, 99045, 58828, 43791, 83190, 20857, 36387, 88536, 51305, 97693, 66113, 36553, 92856, 54215, 16572, 9606, 46113, 75468, 19385, 56154, 16120, 17817, 5890, 5859, 65809, 20672, 13814, 16636, 97021, 42636, 74211, 66307, 4316, 37676, 32250, 17526, 6284, 27026, 56979, 93661, 91742, 98653, 50154, 76810, 69462, 68581, 67154, 79822, 78699, 66615, 67567, 65005, 9940, 41080, 53600, 34426, 76454, 80119, 3554, 15186, 3363, 59412, 49711, 19506, 37429, 74791, 74847, 87222, 11598, 68983, 22805, 82721, 55892, 7826, 62458, 82263, 16744, 25433, 14978, 71486, 14734, 19682, 33166, 15017, 11359, 24933, 88143, 53835, 12530, 95709, 27624, 68806, 44800, 58220, 87446, 69797, 16433, 53064, 66180, 11680, 34777, 56386, 11683, 78150, 32976, 66150, 31854, 95220, 39122, 74876, 93742, 67546, 93618, 84120, 94549, 2763, 17137, 21686, 58226, 51211, 47542, 73619, 19661, 97437, 77, 63928, 48228, 83366, 47037, 60103, 52105, 82124, 44250, 47649, 60102, 98704, 84778, 63420, 48254, 65964, 4857, 33221, 90117, 94301, 98293, 59424, 76079, 56949, 18315, 77536, 4113, 26212, 3140, 81701, 87008, 60925, 95377, 97955, 43447, 61052, 12002, 73819, 72976, 41736, 72983, 82158, 67161, 2872, 56875, 81699, 26259, 10931, 27678, 27167, 6157, 93705, 55331, 3383, 16157, 90502, 81369, 67992, 53511, 69320, 64080, 23009, 73330, 15232, 51354, 98408, 86296, 54742, 36081, 20098, 42555, 97064, 64113, 5828, 28764, 16349, 39219, 85454, 95305, 10819, 44913, 59215, 54077, 53818, 32383, 301, 1026, 3148, 80451, 63501, 64048, 30960, 9441, 23835, 75676, 65616, 39085, 43538, 40571, 46396, 96172, 68011, 16092, 62003, 98990, 26469, 55920, 89469, 99180, 86023, 59281, 55599, 90869, 13737, 50868, 78340, 50068, 65706, 12386, 74264, 4073, 75734, 777, 93898, 94870, 20980, 41404, 66534, 74979, 88901, 55588, 93959, 34752, 63985, 59622, 28147, 15685, 21086, 32668, 69253, 61205, 3576, 73041, 83732, 66515, 5649, 39206, 66894, 51575, 46141, 77238, 47132, 48952, 54236, 42339, 10166, 65240, 1095, 5894, 67133, 5376, 81146, 41801, 15438, 31222, 51736, 4993, 97098, 51817, 31396, 85935, 83795, 69221, 41456, 42975, 93417, 88617, 51169, 82396, 647, 50400, 35947, 80437, 23501, 36876, 12782, 96740, 15047, 69426, 77543, 3082, 41081, 55086, 57617, 97327, 23555, 96317, 24071, 46745, 96534, 56524, 39684, 79222, 37168, 82169, 62059, 92583, 5103, 99918, 29557, 30064, 84558, 19897, 75634, 73189, 55275, 44720, 59802, 45120, 91045, 97055, 35425, 35450, 64528, 16760, 94448, 12714, 48298, 64951, 70010, 55418, 12277, 70615, 81165, 69373, 85208, 96037, 47985, 76353, 88660, 30514, 40638, 10763, 88374, 64626, 15936, 92659, 19560, 39878, 93062, 46639, 60651, 40137, 79501, 71259, 69644, 83455, 76025, 86024, 30269, 4453, 14392, 68915, 98553, 29519, 18659, 97538, 77789, 87016, 25859, 28209, 83427, 64878, 94899, 89298, 41101, 23079, 66057, 19865, 9810, 28283, 69793, 84531, 61272, 36011, 4880, 76350, 80721, 62213, 2721, 11219, 23943, 89486, 47593, 44234, 55779, 22096, 68782, 88650, 79849, 96605, 31093, 28902, 34707, 91465, 38222, 60071, 1745, 9227, 21382, 68078, 51017, 24012, 15342, 21853, 46265, 76142, 58377, 78271, 3416, 91832, 21619, 80199, 76043, 77363, 83027, 45360, 91433, 95269, 59459, 63150, 55402, 54332, 45044, 49051, 69890, 43750, 76601, 79723, 86269, 34771, 37884, 53252, 99940, 8020, 42565, 12553, 32902, 45542, 83006, 52700, 77403, 52065, 24260, 47222, 71522, 83887, 39822, 20793, 38302, 56612, 13561, 15503, 34614, 33940, 32979, 16392, 11631, 92402, 94766, 19220, 64677, 8324, 85056, 51804, 8873, 7104, 62218, 50026, 63515, 14897, 13351, 91761, 47912, 50168, 46584, 23025, 80212, 33198, 67252, 42691, 78736, 98932, 9085, 25587, 98629, 45434, 95164, 20595, 7568, 19137, 58723, 42803, 37611, 50322, 75305, 17731, 52435, 44260, 81656, 34240, 54666, 99087, 99633, 20965, 5657, 61526, 77431, 64439, 7291, 88879, 91450, 84484, 81006, 30030, 10591, 85891, 32773, 77965, 97018, 60073, 96164, 47556, 66144, 73953, 25932, 93371, 64082, 29746, 37442, 25904, 32256, 70407, 69319, 90878, 74056, 95157, 42692, 2192, 96248, 29953, 20077, 5333, 82509, 29187, 11377, 59042, 67696, 1105, 35823, 55048, 27732, 61293, 93587, 50528, 38004, 86416, 39316, 35807, 67108, 23718, 39140, 95070, 69278, 1425, 98635, 89527, 86355, 43369, 97375, 71028, 39233, 37715, 45688, 2498, 15413, 62404, 85458, 52453, 17469, 42955, 14491, 11804, 2399, 47582, 53539, 79843, 53545, 95766, 80011, 8744, 21488, 34659, 80159, 17320, 22480, 92158, 33944, 14412, 72004, 27259, 17439, 15579, 12961, 13350, 85183, 38714, 36189, 42283, 4762, 99320, 64695, 43167, 83260, 77520, 49131, 65470, 63315, 75894, 33935, 30669, 8644, 93874, 43180, 85952, 90723, 65002, 28168, 70846, 58572, 11055, 53507, 10259, 89401, 59865, 61424, 76525, 48226, 41744, 34869, 73297, 69018, 37537, 10732, 21674, 26245, 35756, 23150, 59221, 69407, 98666, 65548, 92574, 51204, 48719, 54271, 77333, 60428, 74450, 14406, 58584, 18556, 38416, 48225, 1098, 61085, 54245, 9311, 54828, 65555, 64872, 66038, 44454, 68989, 267, 42213, 82394, 46772, 54617, 43013, 43494, 77631, 77079, 81801, 70218, 16720, 39735, 56666, 63183, 43419, 3835, 48236, 21978, 47859, 3621, 92442, 92637, 85926, 50899, 88442, 10832, 25280, 62966, 46741, 81781, 22603, 66149, 30321, 16377, 94912, 83089, 14343, 58180, 55174, 64317, 91644, 77060, 25110, 77067, 77529, 5033, 62829, 65498, 13442, 87092, 70674, 60327, 41477, 45679, 74690, 22996, 77595
```

## Bare Metal (native)
Using Python 3.6 Flask and Flask-restful API
1. Create Virtual Environment and install 
	```bash
	virtualenv <environment>
	```
	Active environment
	```bash
	source avg/bin/activate
	```
	Install flask and flask-restful via pip3
	```bash
	pip3 install flask
	pip3 install flask-restful
	```
2. Run Python API server (via Flask or Flask-restful)
- Flask native ([https://github.com/pallets/flask](https://github.com/pallets/flask))
	```bash
	export FLASK_APP=baremetal/flask-native.py
	python -m flask run
	```
	URL after deployed:
	1. Average: `<IP Server>:5000/avg`
	2. Merge sort: `<IP Server>:5000/merge`
	3. Bubble sort: `<IP Server>:5000/bubble`
- Flask RESTful ([https://flask-restful.readthedocs.io/en/latest/](https://flask-restful.readthedocs.io/en/latest/))
	```python
	python baremetal/restful-flask-native.py
	```
	URL after deployed:
	1. Average: `<IP Server>:8000/avg`
	2. Merge sort: `<IP Server>:8000/merge`
	3. Bubble sort: `<IP Server>:8000/bubble`

## OpenFaaS (serverless)
### Get templates
1. Of-watchdog: Python3 Flask - HTTP [https://github.com/openfaas-incubator/of-watchdog](https://github.com/openfaas-incubator/of-watchdog) 
	```bash
	faas template store pull python3-http
	```
2. Classic watchdog: Python3 [https://github.com/openfaas/templates](https://github.com/openfaas/templates)
	```bash
	 faas template store pull python3
	```

### Create new project
Create new project
```bash
faas-cli new --lang <language-name> <funtions-name> --prefix="<docker-username>"
```
Sample .yml file
```bash
version: 1.0
provider:
  name: openfaas
  gateway: http://192.168.1.9:31112
functions:
  mergesort-of:
    lang: python3-http
    handler: ./mergesort-of
    image: itbiboo/mergesort-of:latest
    labels:
      com.openfaas.scale.min: 1
      com.openfaas.scale.max: 1
      com.openfaas.scale.factor: 100
```
**Note**: Turn off autoscaling and manually adjust the number of pods (1, 5 and 10).
### Build, deploy and push
```bash
faas-cli up -f <yml file>
```
1. **Of-watchdog**:
- Average: `openfaas/avg-of-watchdog`
	URL: `<IP Server>:31112/function/avg-of`
- Merge sort: `openfaas/merge-of-watchdog`
	URL: `<IP Server>:31112/function/mergesort-of`
- Bubble sort: `openfaas/bubble-of-watchdog`
	URL: `<IP Server>:31112/function/bubblesort-of`
2. **Classic**:
- Average: `openfaas/avg-classic`
	URL: `<IP Server>:31112/function/avg-classic`
- Merge sort: `openfaas/merge-classic`
	URL: `<IP Server>:31112/function/merge-classic`
- Bubble sort: `openfaas/bubble-classic`
	URL: `<IP Server>:31112/function/bubble-classic`

## Testing 
Using hey ([https://github.com/rakyll/hey](https://github.com/rakyll/hey))
```bash
hey -m POST -D input.txt -n 1000 -c 100 <URL>
```
### Test workflow:
1. Using hey from another computer (MacBook Pro 2017 MPTT2) on same LAN send load to Server with each URL candidates (one by one, using same input numbers, same parameter of hey)
2. Compare:
	- Total complete time
	- Average complete time of 1 request
	- Request/second
	- Resources consumption
3. Adjust some parameters  and do step 1,2 again
	- Changing number of request: `-n (500, 1000)`
	- Change number or concurrently request:  `-c (100, 50)`
	- Change number of pod replicas: 1, 5, 10
		```bash
		    labels:
			  com.openfaas.scale.min: <1,5,10>
			  com.openfaas.scale.max: <1,5,10>
			  com.openfaas.scale.factor: 100
		```

### Measure CPU/RAM on baremetal
Using psrecord ([https://github.com/astrofrog/psrecord](https://github.com/astrofrog/psrecord))
```bash
pip install psrecord
```
Record CPU and memory and plot
```bash
psrecord <pid> --log activity.txt --plot plot.png
```

### Measure CPU/RAM on OpenFaas functions
…

### Preliminary results
Merge sort, 1000 input numbers
```bash
hey -n 1000 -c 100 -d "$INPUTTEST" <API_URL>
```
#### Bare metal (Flask native)
```bash
% hey -D input.txt -m POST -n 1000 -c 100 http://192.168.1.9:5000/merge

Summary:
  Total:        11.3759 secs
  Slowest:      1.8359 secs
  Fastest:      0.0322 secs
  Average:      1.0745 secs
  Requests/sec: 87.9049
  
  Total data:   5903000 bytes
  Size/request: 5903 bytes

Response time histogram:
  0.032 [1]     |
  0.213 [33]    |■■■■■■
  0.393 [24]    |■■■■
  0.573 [28]    |■■■■■
  0.754 [103]   |■■■■■■■■■■■■■■■■■
  0.934 [240]   |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  1.114 [124]   |■■■■■■■■■■■■■■■■■■■■■
  1.295 [118]   |■■■■■■■■■■■■■■■■■■■■
  1.475 [117]   |■■■■■■■■■■■■■■■■■■■■
  1.656 [116]   |■■■■■■■■■■■■■■■■■■■
  1.836 [96]    |■■■■■■■■■■■■■■■■


Latency distribution:
  10% in 0.6001 secs
  25% in 0.7932 secs
  50% in 1.0302 secs
  75% in 1.3982 secs
  90% in 1.6514 secs
  95% in 1.7375 secs
  99% in 1.8017 secs

Details (average, fastest, slowest):
  DNS+dialup:   0.0035 secs, 0.0322 secs, 1.8359 secs
  DNS-lookup:   0.0000 secs, 0.0000 secs, 0.0000 secs
  req write:    0.0001 secs, 0.0000 secs, 0.0029 secs
  resp wait:    1.0650 secs, 0.0278 secs, 1.8304 secs
  resp read:    0.0058 secs, 0.0000 secs, 0.0654 secs

Status code distribution:
  [200] 1000 responses
```

#### Bare metal (Flask RESTful)
```bash
% hey -D input.txt -m POST -n 1000 -c 100 http://192.168.1.9:8000/merge

Summary:
  Total:        10.7246 secs
  Slowest:      1.8677 secs
  Fastest:      0.0400 secs
  Average:      1.0332 secs
  Requests/sec: 93.2439
  
  Total data:   5903000 bytes
  Size/request: 5903 bytes

Response time histogram:
  0.040 [1]     |
  0.223 [30]    |■■■■■■
  0.406 [15]    |■■■
  0.588 [52]    |■■■■■■■■■■■
  0.771 [186]   |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.954 [178]   |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  1.137 [126]   |■■■■■■■■■■■■■■■■■■■■■■■■■■■
  1.319 [130]   |■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  1.502 [151]   |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  1.685 [91]    |■■■■■■■■■■■■■■■■■■■■
  1.868 [40]    |■■■■■■■■■


Latency distribution:
  10% in 0.6034 secs
  25% in 0.7379 secs
  50% in 1.0089 secs
  75% in 1.3621 secs
  90% in 1.5715 secs
  95% in 1.6693 secs
  99% in 1.7756 secs

Details (average, fastest, slowest):
  DNS+dialup:   0.0026 secs, 0.0400 secs, 1.8677 secs
  DNS-lookup:   0.0000 secs, 0.0000 secs, 0.0000 secs
  req write:    0.0001 secs, 0.0000 secs, 0.0013 secs
  resp wait:    1.0249 secs, 0.0358 secs, 1.8315 secs
  resp read:    0.0056 secs, 0.0000 secs, 0.0766 secs

Status code distribution:
  [200] 1000 responses
```

#### OpenFaas - of-watchdog (1 pod)
```bash
% hey -D input.txt -m POST -n 1000 -c 100 http://192.168.1.9:31112/function/mergesort-of 

Summary:
  Total:        4.1763 secs
  Slowest:      3.6683 secs
  Fastest:      0.0067 secs
  Average:      0.2618 secs
  Requests/sec: 239.4455
  
  Total data:   6901000 bytes
  Size/request: 6901 bytes

Response time histogram:
  0.007 [1]     |
  0.373 [904]   |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.739 [24]    |■
  1.105 [12]    |■
  1.471 [9]     |
  1.837 [8]     |
  2.204 [11]    |
  2.570 [4]     |
  2.936 [2]     |
  3.302 [12]    |■
  3.668 [13]    |■


Latency distribution:
  10% in 0.0549 secs
  25% in 0.0813 secs
  50% in 0.0948 secs
  75% in 0.1291 secs
  90% in 0.3423 secs
  95% in 1.4937 secs
  99% in 3.4645 secs

Details (average, fastest, slowest):
  DNS+dialup:   0.0008 secs, 0.0067 secs, 3.6683 secs
  DNS-lookup:   0.0000 secs, 0.0000 secs, 0.0000 secs
  req write:    0.0001 secs, 0.0000 secs, 0.0014 secs
  resp wait:    0.2600 secs, 0.0061 secs, 3.6675 secs
  resp read:    0.0008 secs, 0.0001 secs, 0.0052 secs

Status code distribution:
  [200] 1000 responses
```

#### OpenFaas - classic watchdog (1 pod)
```bash
% hey -D input.txt -m POST -n 1000 -c 100 http://192.168.1.9:31112/function/merge-classic

Summary:
  Total:        4.6816 secs
  Slowest:      3.1830 secs
  Fastest:      0.0265 secs
  Average:      0.4171 secs
  Requests/sec: 213.6014
  

Response time histogram:
  0.026 [1]     |
  0.342 [389]   |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.658 [525]   |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.973 [76]    |■■■■■■
  1.289 [2]     |
  1.605 [0]     |
  1.920 [2]     |
  2.236 [1]     |
  2.552 [1]     |
  2.867 [2]     |
  3.183 [1]     |


Latency distribution:
  10% in 0.2290 secs
  25% in 0.3063 secs
  50% in 0.3702 secs
  75% in 0.5044 secs
  90% in 0.6228 secs
  95% in 0.7484 secs
  99% in 0.9314 secs

Details (average, fastest, slowest):
  DNS+dialup:   0.0008 secs, 0.0265 secs, 3.1830 secs
  DNS-lookup:   0.0000 secs, 0.0000 secs, 0.0000 secs
  req write:    0.0001 secs, 0.0000 secs, 0.0007 secs
  resp wait:    0.4156 secs, 0.0259 secs, 3.1765 secs
  resp read:    0.0005 secs, 0.0000 secs, 0.0044 secs

Status code distribution:
  [200] 1000 responses
```

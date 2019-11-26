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
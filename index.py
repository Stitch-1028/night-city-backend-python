from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources=r'/*')


@app.route("/api/v1/python/get", methods=['GET'])
def python_get():
    try:
        name = request.args.get('name')
        print(name)
        return jsonify({"code": 0, "data": {"message": f"你好哇! {name} 你刚刚调用了Python的GET接口"}})
    except:
        return jsonify({"code": 1, "data": {"msg": "调用失败"}})


@app.route("/api/v1/python/post", methods=['POST'])
def python_post():
    try:
        name = request.json['name']
        return jsonify({"code": 0, "data": {"message": f"你好哇! {name} 你刚刚调用了Python的POST接口"}})
    except:
        return jsonify({"code": 1, "data": {"msg": "调用失败"}})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)
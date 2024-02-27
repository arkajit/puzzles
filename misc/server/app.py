from flask import Flask, render_template, request, jsonify
import redis
app = Flask(__name__)

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
count = 0

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/hi')
def hi():
    name = request.args.get('name', 'visitor')
    return f'Hi, {name}! Nice to meet you! How are you?'

@app.route('/set', methods=['POST'])
def set_key():
    data = request.get_json()
    key = data.get('key')
    value = data.get('value')
    redis_client.set(key, value)
    return jsonify({'message': 'Key set successfully'})

@app.route('/get/<key>', methods=['GET'])
def get_key(key):
    value = redis_client.get(key)
    if value is None:
        return jsonify({'error': 'Key not found'}), 404
    else:
        return jsonify({'key': key, 'value': value.decode('utf-8')})

if __name__ == '__main__':
    app.run(debug=True)


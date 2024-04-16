from flask import Flask, render_template, request, json, jsonify, g, abort
import threading
import redis
app = Flask(__name__)

# QuestionDB is protected by a mutex for concurrent thread access.
class QuestionDB(object):
    def __init__(self):
        print(f"Constructing a QuestionDB!")
        self.questions = list()
        self._lock = threading.Lock()
        self._qid = 0

    def nextId(self):
        self._qid += 1
        return self._qid

    def addQuestion(self, q):
        self._lock.acquire()

        try:
            q.qid = self.nextId()
            self.questions.append(q)
        finally:
            self._lock.release()

    def getQuestions(self, start=0, size=100):
        if start > len(self.questions):
            return []
        return self.questions[start:start+size]

question_db = QuestionDB()

# Question: creator is user email
class Question(object):
    def __init__(self, title, content, creator):
        print(f"Creating question!")
        self.qid = None
        self.title = title
        self.content = content
        self.creator = creator

    def isValid(self):
        return self.title is not None and self.content is not None and self.creator is not None

    def getJson(self):
        return {
            "questionId": self.qid,
            "title": self.title,
            "content": self.content,
            "creator": self.creator
        }

class QuestionJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Question):
            return obj.getJson()
        return super().default(obj)
app.json_encoder = QuestionJSONEncoder

@app.errorhandler(400)
def invalid_request_error(error):
    return jsonify({'result': 'error', 'message': str(error)})

@app.route('/questions', methods=['POST'])
def create_question():
    data = request.get_json()

    # NOTE: do request validation
    title = data.get('title')
    content = data.get('content')
    creator = data.get('creator')
    question = Question(title, content, creator)
    if question.isValid():
        question_db.addQuestion(question)
        return jsonify({'result': 'Success'})
    else:
        abort(400)

@app.route('/questions', methods=['GET'])
def list_questions():
    offset_qid = request.args.get('qid')
    if offset_qid is None:
        offset_qid = 1
    else:
        offset_qid = int(offset_qid)

    page_size = 2
    qs = question_db.getQuestions(start=offset_qid-1, size=page_size)
    return jsonify(qs)

####

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


from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import storage                       # módulo acima

app = Flask(__name__, static_folder='../frontend')
CORS(app)


# ---------- rotas ----------
@app.get('/api/score')
def get_score():
    return jsonify({'score': storage.load_score()})


@app.post('/api/click')
def click():
    data  = request.get_json(silent=True) or {}
    delta = int(data.get('delta', 1))
    new_score = storage.inc_score(delta)
    return jsonify({'score': new_score})


@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path:path>')
def front(path):
    return send_from_directory('../frontend', path)


if __name__ == '__main__':
    # threaded=True permite várias conexões simultâneas
    app.run(host='0.0.0.0', port=8000, threaded=True)